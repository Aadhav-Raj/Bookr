from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PublisherForm, SearchForm, ReviewForm,BookMediaForm
from .models import Book, Contributor, Publisher, Review
from .utils import average_rating
from PIL import Image
from io import BytesIO
from django.core.files.images import  ImageFile
from django.contrib.auth.decorators import login_required,user_passes_test

def index(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()
    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            fname_contributors = \
                Contributor.objects.filter(first_names__icontains=search)

            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

            lname_contributors = \
                Contributor.objects.filter(last_names__icontains=search)

            for contributor in lname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

    return render(request, "search-results.html", {"form": form, "search_text": search_text, "books": books})


def book_list(request):
    books = Book.objects.all()
    books_with_reviews = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        books_with_reviews.append({"book": book, "book_rating": book_rating, "number_of_reviews": number_of_reviews})

    context = {


    "book_list": books_with_reviews
    }
    #< a class ="btn btn-primary" href="{% url 'review_create' book.pk %}" > Add Review < / a >
    #<!--<a class="btn btn-primary" href="{% url 'review_create' book.pk %}">Add Review</a>-->

    #<!--<a href="{% url 'review_edit' book.pk review.pk %}">Edit Review</a>-->

    return render(request, "list.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {
            "book": book,
            "book_rating": book_rating,
            "reviews": reviews
        }
    else:
        context = {
            "book": book,
            "book_rating": None,
            "reviews": None
        }
    if request.user.is_authenticated:
        max_viewed_books_length = 10
        viewed_books = request.session.get('viewed_books', [])
        viewed_book = [book.id, book.title]
        if viewed_book in viewed_books:
            viewed_books.pop(viewed_books.index(viewed_book))
        viewed_books.insert(0, viewed_book)
        viewed_books = viewed_books[:max_viewed_books_length]
        request.session['viewed_books'] = viewed_books
    return render(request, "book_detail.html", context)


def is_staff_user(user):
    return user.is_staff
@user_passes_test(is_staff_user)
def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, "Publisher \"{}\" was created.".format(updated_publisher))
            else:
                messages.success(request, "Publisher \"{}\" was updated.".format(updated_publisher))

            return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)

    return render(request, "instance-form.html",
                  {"form": form, "instance": publisher, "model_type": "Publisher"})



@login_required
#@user_passes_test(is_staff_user)
def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)

    if review_pk is not None:
        review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
        user=request.user
        if not user.is_staff and review.creator.id !=user.id:
           raise PermissionError

    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            updated_review = form.save(False)
            updated_review.book = book

            if review is None:
                messages.success(request, "Review for \"{}\" created.".format(book))
            else:
                updated_review.date_edited = timezone.now()
                messages.success(request, "Review for \"{}\" updated.".format(book))

            updated_review.save()
            return redirect("book_detail", book.pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, "instance-form.html",
                  {"form": form,
                   "instance": review,
                   "model_type": "Review",
                   "related_instance": book,
                   "related_model_type": "Book"
                })

@login_required
@user_passes_test(is_staff_user)
def book_media(request,pk):
    book=get_object_or_404(Book,pk=pk)

    if request.method=="POST":
        form=BookMediaForm(request.POST,request.FILES,instance=book)

        if form.is_valid():
            book=form.save(False)
            cover=form.cleaned_data.get("cover")

            if cover:
                image=Image.open(cover)
                image.thumbnail((300,300))
                image_data=BytesIO()
                image.save(fp=image_data,format=cover.image.format)
                image_file=ImageFile(image_data)
                book.cover.save(cover.name,image_file)
            book.save()
            messages.success(request,"Book \"{}\" was successfully updated.".format(book))
            return redirect("book_detail", book.pk)
    else:
        form = BookMediaForm(instance=book)
    return render(request, "instance-form.html",
                  {"instance": book, "form": form, "model_type": "Book", "is_file_upload": True})

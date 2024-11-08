from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book,Review
# for ex:12.3 from .serializers import BookSerializer,BookSerializer2
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .serializers import BookSerializer, ReviewSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView


class Login(APIView):
    def post(self,request):
        user=authenticate(username=request.data.get("username"),password=request.data.get("password"))

#curl.exe -X GET http://127.0.0.1:8000/api/books/ -H "Authorization: Token 76565c0f6ff3be1b52c1681e6360d4af91df7391"
        if not user:
            return Response({"error":"Credentials are incorrect"},status=HTTP_404_NOT_FOUND)
        token, _ =Token.objects.get_or_create(user=user)
        return Response({"token":token.key},status=HTTP_200_OK)
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.order_by('-date_created')
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = []

    """
    for ex:12.3
class AllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer2
    """
    """
for ex:12.2
@api_view()
def all_books(request):
    books=Book.objects.all()
    book_serializer=BookSerializer(books, many=True)
    return Response(book_serializer.data)
"""
"""
for ex:12.1
@api_view()
def first_api_view(request):
    num_books=Book.objects.count()
    return Response({"num_books":num_books})

"""
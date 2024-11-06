from django.urls import path
from . import views,api_views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)

urlpatterns=[path('books/',views.book_list,name="book_list"),
             path('search/',views.book_search,name="search"),
             path('book_detail/<int:pk>/',views.book_detail, name='book_detail'),
             path('publisher/<int:pk>',views.publisher_edit, name='publisher_edit'),
             path('publisher/new', views.publisher_edit, name='publisher_create'),
             path('books/<int:book_pk>/new/', views.review_edit, name='review_create'),
             path('books/<int:book_pk>/<int:review_pk>/', views.review_edit, name='review_edit'),
             # path('books/<int:pk>/', views.book_detail, name='book_detail'),
             path('books/<int:pk>/media/', views.book_media, name='book_media'),
            # for ex:12.1 path("api/first_api_view/",api_views.first_api_view),
             # for ex:12.2 path('api/all_books/', api_views.all_books, name='all_books'),
             # for ex:12.3 path('api/all_books2/', api_views.AllBooks.as_view(), name='all_books'),
             path('api/login',api_views.Login.as_view(),name="login"),
             path('api/', include((router.urls, 'api'))),]

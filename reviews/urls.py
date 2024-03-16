from django.urls import path
from . import views

urlpatterns=[path('books/',views.bookList,name="book_list"),
             path('search/',views.book_search,name="search"),
             path('book_detail/<int:pk>/',views.book_detail, name='book_detail'),
             path('publisher/<int:pk>',views.Publisher_edit, name='publisher_edit'),
             path('publisher/new', views.Publisher_edit, name='publisher_create'),
             path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
             path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
             path('books/<int:pk>/', views.book_detail, name='book_detail'),
             ]

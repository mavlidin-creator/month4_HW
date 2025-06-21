from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='new_book'),
    path('', views.book_list_view, name='book_list'),
    path('<int:id>/', views.book_detail_view, name='book_detail'),
    path('new_book/<int:id>/', views.book_detail_view, name='new_book_details'),
    path('books/', views.book, name='books'),
    path('new_book/<int:book_id>/audio/', views.your_view_function, name='audio_recording'),
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from basket import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('new_book/', include('books.urls')),
    path('baskets/', views.basket_list, name='basket_list'),
    path('baskets/create/', views.basket_create, name='basket_create'),
    path('baskets/<int:pk>/update/', views.basket_update, name='basket_update'),
    path('baskets/<int:pk>/delete/', views.basket_delete, name='basket_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

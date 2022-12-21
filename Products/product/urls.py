from django.urls import path
from Products.product import views

urlpatterns = [
    path('get_all/', views.getAllProduct),
    path('get_by_id/<int:pk>/', views.getProductById),
    path('post/', views.createProduct),
    path('put/<int:pk>/', views.updateProduct),
    path('delete/<int:pk>/', views.deleteProduct),
]
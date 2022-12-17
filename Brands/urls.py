from django.urls import path, include
from . import views

urlpatterns = [
    path('get_all/', views.getAllBrand),
    path('get_by_id/<int:pk>/', views.getBrandById),
    path('post/', views.createBrand),
    path('put/<int:pk>/', views.updateBrand),
    path('delete/<int:pk>/', views.deleteBrand),

    path('category/', include('Brands.category.urls')),
]
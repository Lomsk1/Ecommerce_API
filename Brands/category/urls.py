from django.urls import path
from . import views

urlpatterns = [
    path('all_by_brand/<int:brand_id>/', views.getCategoriesByBrand ),
    path('get_by_id/<int:pk>/', views.getBrandCategory),
    path('all/', views.getAllBrandCategory),
    path('create/', views.createBrandCategory),
    path('put/<int:pk>/', views.putBrandCategory),
    path('delete/<int:pk>/', views.deleteBrandCategory),
]
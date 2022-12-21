from django.urls import path
from . import views

urlpatterns = [
    path('all_by_product/<int:product_id>/', views.getSpecificationsByProduct ),
    path('get_by_id/<int:pk>/', views.getSpecificationByID),
    path('all/', views.getAllSpecification),
    path('create/', views.createSpecification),
    path('put/<int:pk>/', views.putSpecification),
    path('delete/<int:pk>/', views.deleteSpecification),
]
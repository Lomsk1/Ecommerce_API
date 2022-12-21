from django.urls import path
from . import views

urlpatterns = [
    path('all_by_product/<int:product_id>/', views.getImagesByProduct ),
    path('get_by_id/<int:pk>/', views.getImagesByID),
    path('all/', views.getAllImages),
    path('create/', views.createImage),
    path('put/<int:pk>/', views.putImage),
    path('delete/<int:pk>/', views.deleteImage),
]
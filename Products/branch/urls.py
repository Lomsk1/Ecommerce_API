from django.urls import path
from . import views

urlpatterns = [
    path('all_by_product/<int:product_id>/', views.getStockByProduct ),
    path('get_by_id/<int:pk>/', views.getStockByID),
    path('all/', views.getAllStock),
    path('create/', views.createStock),
    path('put/<int:pk>/', views.putStock),
    path('delete/<int:pk>/', views.deleteStock),
]
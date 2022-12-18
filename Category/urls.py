from django.urls import path, include
from Category import views

urlpatterns = [
    path('get_all/', views.getAllCategory),
    path('get_by_id/<int:pk>/', views.getCategoryByID),
    path('create/', views.createCategory),
    path('put/<int:pk>/', views.changeCategory),
    path('delete/<int:pk>/', views.deleteCategory),
]
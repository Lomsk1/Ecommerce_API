from django.urls import path
from . import views

urlpatterns = [
    path('all_by_product/<int:basic_id>/', views.getSpecBasicBySpec ),
    path('get_by_id/<int:pk>/', views.getSpecBasicByID),
    path('all/', views.getAllSpecBasic),
    path('create/', views.createSpecBasic),
    path('put/<int:pk>/', views.putSpecBasic),
    path('delete/<int:pk>/', views.deleteSpecBasic),
]
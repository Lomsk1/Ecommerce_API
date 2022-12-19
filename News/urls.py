from django.urls import path
from News import views

urlpatterns = [
    path('get_all/', views.newsAll),
    path('get_by_id/<int:pk>/', views.newsByID),
    path('post/', views.createNews),
    path('put/<int:pk>/', views.changeNews),
    path('delete/<int:pk>/', views.deleteNews),
]
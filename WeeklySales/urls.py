from django.urls import path
from WeeklySales import views

urlpatterns = [
    path('get_all/', views.getAllWeekly),
    path('get_by_id/<int:pk>/', views.getWeeklyById),
    path('post/', views.createWeekly),
    path('put/<int:pk>/', views.updateWeekly),
    path('delete/<int:pk>/', views.deleteWeekly),
]
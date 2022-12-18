from django.urls import path
from Branch.working_hours import views

urlpatterns = [
    path('get_all/', views.getAllWorkingHours),
    path('get_by_id/<int:pk>/', views.getWorkingHoursByID),
    path('get_by_Branch/<int:branch_id>/', views.getWorkingHoursByBranch),
    path('post/', views.createBranchWorkingHours),
    path('put/<int:pk>/', views.putBranchWorkingHours),
    path('delete/<int:pk>/', views.deleteBranchWorkingHours),
]
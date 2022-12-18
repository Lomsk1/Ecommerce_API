from django.urls import path
from Branch.branch import views

urlpatterns = [
    path('get_all/', views.getAllBranch),
    path('get_by_id/<int:pk>/', views.getBranchByID),
    path('post/', views.createBranch),
    path('put/<int:pk>/', views.putBranch),
    path('delete/<int:pk>/', views.deleteBranch),
]
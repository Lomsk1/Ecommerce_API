from django.urls import path
from Branch.coord import views

urlpatterns = [
    path('get_all/', views.getAllBranchCoord),
    path('get_by_id/<int:pk>/', views.getBranchCoordByID),
    path('get_by_Branch/<int:branch_id>/', views.getBranchCoordByBranch),
    path('post/', views.createBranchCoord),
    path('put/<int:pk>/', views.putBranchCoord),
    path('delete/<int:pk>/', views.deleteBranchCoord),
]
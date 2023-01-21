from django.urls import path
from wishlist import views

urlpatterns = [
    path('get_all/', views.getAllWishlist),
    path('get_by_id/<int:pk>/', views.getWishlistById),
    path('get_by_user/<int:user_id>/', views.getWishlistByUser),
    path('post/', views.createWishlist),
    path('put/<int:pk>/', views.updateWishlist),
    path('delete/<int:pk>/', views.deleteWishlist),
]
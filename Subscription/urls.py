from django.urls import path
from Subscription import views

urlpatterns = [
    path('get_all/', views.getAllSubscriptions),
    path('get_by_id/<int:pk>/', views.getSubscriptionsById),
    path('post/', views.createSubscriptions),
    path('put/<int:pk>/', views.updateSubscriptions),
    path('delete/<int:pk>/', views.deleteSubscriptions),
]
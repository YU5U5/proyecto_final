from django.urls import path
from . import views

urlpatterns = [
    path('create_fish/', views.CreateFish.as_view(), name='create_fish'),
    path('update_fish/', views.UpdateFish.as_view(), name='update_fish'),
    path('list_fish/', views.List.as_view(), name='delete_fish'),
    path('details_fish/<int:pk>/', views.Details.as_view(), name='details_fish'),
]   
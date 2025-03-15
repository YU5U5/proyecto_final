from django.urls import path
from . import views

urlpatterns = [
    path('create_procedimiento/', views.CreateProcedimiento.as_view(), name='create_procedimiento'),
    path('update_procedimiento/', views.UpdateProcedimiento.as_view(), name='update_procedimiento'),
    path('list_procedimiento/', views.List.as_view(), name='delete_procedimiento'),
    path('details_procedimiento/<int:pk>/', views.Details.as_view(), name='details_procedimiento'),
]
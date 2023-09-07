from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-row/', views.createRow, name='create-row'),
    path('update-row/<str:pk>/', views.updateRow, name = "update-row"),
    path('delete-row/<pk>/', views.deleteRow, name = "delete-row"),
]

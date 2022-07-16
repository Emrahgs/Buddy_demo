from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.getRooms, name='getRooms'),
    path('rooms/<int:pk>/', views.getRoom, name='getRoom'),
]
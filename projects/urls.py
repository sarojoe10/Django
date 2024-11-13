from django.urls import path
from .views import *





urlpatterns = [
    path('',projects),
    path('projects/', projects),
    path('projects/<str:pk>', project)
]
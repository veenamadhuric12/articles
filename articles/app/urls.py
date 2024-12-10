from django.urls import path
from . import views

urlpatterns = [
    path('a',views.index),
    path('one/<int:pk>',views.details,name = "details")
]
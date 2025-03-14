from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.serve_random_music, name='serve_random_music'),
]
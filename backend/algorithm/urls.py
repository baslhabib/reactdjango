from django.urls import path
from .views import run_algorithm

urlpatterns = [
    path('run/', run_algorithm, name='run_algorithm'),  # This creates the URL path for your view
]

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('recommended/', views.recommended, name='recommended'),
]

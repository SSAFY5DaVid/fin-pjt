from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles),
    path('<int:pk>/', views.article_detail),
    path('comments/', views.comments),
    path('comments/<int:pk>/', views.comment_detail),
    path('<int:article_pk>/comments/', views.article_comments),
]

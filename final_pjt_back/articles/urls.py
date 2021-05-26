from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles),
    path('<int:pk>/', views.article_detail),
    path('comments/', views.comments),
    path('comments/<int:pk>/', views.comment_detail),
    path('<int:article_pk>/comments/', views.article_comments),
    path('movie_review_list_create/',views.movie_review_list_create),
    path('movie_review_delete/<int:movie_review_pk>/',views.movie_review_delete),
]

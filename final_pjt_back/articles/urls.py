from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('movie_review_list_create/',views.movie_review_list_create),
    path('movie_review_list_order_by_like/',views.movie_review_list_order_by_like),
    path('movie_review_update_delete/<int:movie_review_pk>/',views.movie_review_update_delete),
    # path('movie_review_comment_create/<int:movie_review_pk>/',views.movie_review_comment_create),
    # path('movie_review_comment_delete/<int:comment_pk>/',views.movie_review_comment_delete),
    
    # path('get_user_movie_reviews/<int:movie_review_pk>/',views.get_user_movie_reviews),
    # path('get_user_reviews/',views.get_user_reviews),
    # path('get_movie_review_comments/<int:movie_review_pk>/',views.get_movie_review_comments),
    # path('like_movie_review/<int:movie_review_pk>/',views.like_movie_review),
    



    path('', views.articles),
    path('<int:pk>/', views.article_detail),
    path('comments/', views.comments),
    path('comments/<int:pk>/', views.comment_detail),
    path('<int:article_pk>/comments/', views.article_comments),
]

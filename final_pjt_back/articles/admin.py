from django.contrib import admin
from .models import MovieReview, Article, Comment

# Register your models here.
admin.site.register(MovieReview)
admin.site.register(Article)
admin.site.register(Comment)

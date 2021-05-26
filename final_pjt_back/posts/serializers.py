from rest_framework import serializers
from .models import Post


# List 불러올 때 사용하는 Serializer 
class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
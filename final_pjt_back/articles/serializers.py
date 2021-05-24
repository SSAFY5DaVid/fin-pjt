from rest_framework import serializers
from .models import Article, Comment, MovieReview

# List 불러올 때 사용하는 Serializer 
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__' # 필요한 것만 불러올 수 있음 ('id', 'title')
        


class CommentSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    comment_set = CommentSerializer(read_only=True, many=True) # read_only 유효성 검사 하지 않기 위해 사용 
    comment_count = serializers.IntegerField(read_only=True, source='comment_set.count')
    
    class Meta:
        model = Article
        fields = '__all__' 
        read_only_fields = ('user',)


class MovieReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovieReview
        # 'like',
        # fields = ('username','id', 'rank', 'content', 'movie_title', 'title','created_at')
        fields = '__all__'
        read_only_fields = ('title','user',)
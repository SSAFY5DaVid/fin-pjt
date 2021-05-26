from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication 

from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Article, Comment, MovieReview
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, MovieReviewSerializer




@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_review_list_create(request):
    if request.method == 'GET':
        movie_reviews = MovieReview.objects.all().order_by('-created_at')
        serializer = MovieReviewSerializer(movie_reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = MovieReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_review_delete(request, movie_review_pk):
    movie_review = get_object_or_404(MovieReview, pk=movie_review_pk)
    movie_review.delete()
    return Response({ 'id': movie_review_pk })


@api_view(['GET', 'POST']) # response 쓸때 해당 decorator 필수
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def articles(request):
    if request.method == 'GET':
        article_list = get_list_or_404(Article)
        serializer = ArticleListSerializer(article_list, many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED) # status=201 도 가능
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT']) # response 쓸때 해당 decorator 필수
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        # article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else: # DELETE
        # article = get_object_or_404(Article, pk=pk)
        article.delete()
        response = {'pk':pk}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comments(request):
    comment_list = get_list_or_404(Comment)
    serializer = CommentSerializer(comment_list, many=True)
    return Response(serializer.data)


@api_view(['GET','DELETE']) # response 쓸때 해당 decorator 필수
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': pk })


@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_comments(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        comment_list = article.comment_set.all()
        serializer = CommentSerializer(comment_list, many=True)
        return Response(serializer.data)
    else:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)




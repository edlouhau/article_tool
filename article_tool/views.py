from django.http import JsonResponse
from articles_api.models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse({'articles': serializer.data})
    
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request,id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        pass
    
    elif request.method == 'DELETE':
        pass
       

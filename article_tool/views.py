from django.http import JsonResponse
from articles_api.models import Article
from .serializers import ArticleSerializer

def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse({'articles': serializer.data}, safe=False)


from rest_framework import serializers
from articles_api.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','url','title', 'reading_time', 'summary', 'notes', 'related_links'] 
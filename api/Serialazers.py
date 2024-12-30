from .models import Blog
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content',
                  'image_url', 'posted_by', 'post_date']

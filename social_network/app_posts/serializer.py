from rest_framework import serializers
from .models import PostClass


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostClass
        fields = ('Post_id', 'Title_post')

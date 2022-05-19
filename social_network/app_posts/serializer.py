from rest_framework import serializers
from .models import PostClass


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostClass
        fields = '__all__'
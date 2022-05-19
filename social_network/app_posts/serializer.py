from rest_framework import serializers
from .models import PostClass


class PostSerializer(serializers.ModelSerializer):
    Author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PostClass
        fields = '__all__'

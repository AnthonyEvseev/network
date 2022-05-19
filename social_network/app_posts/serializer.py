from rest_framework import serializers
from .models import PostClass


class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PostClass
        fields = '__all__'

from rest_framework import serializers

from app.models import User, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'liked', 'unliked', 'total_liked','created_at', 'author']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

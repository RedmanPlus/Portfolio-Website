from rest_framework import serializers
from .models import Project, Post

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        depth = 1

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
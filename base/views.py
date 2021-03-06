from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer, ProjectShortenSerializer

# Create your views here.
class ListProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ListProjectShortenView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectShortenSerializer
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListProjectShortenView.as_view(), name='index'),
    path('projects/', views.ListProjectView.as_view(), name='project')
]
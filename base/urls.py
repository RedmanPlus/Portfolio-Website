from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListProjectView.as_view(), name='index'),
]
from rest_framework import serializers
from .models import Project, Post, Screenshot

class ProjectSerializer(serializers.ModelSerializer):

	class Meta:
		model = Project
		# fields = '__all__'
		exclude = ('id',)
		depth = 1

	def to_representation(self, instance):
		rep = super(ProjectSerializer, self).to_representation(instance)

		rep['stack'] = [technology.name for technology in instance.stack.all()]
		rep['contributors'] = [[one.name, one.link] for one in instance.contributors.all()]

		return rep

class ProjectShortenSerializer(serializers.ModelSerializer):

	class Meta:
		model = Project
		fields = ['id', 'add_date', 'name', 'stack']
		depth = 1

	def to_representation(self, instance):
		rep = super(ProjectShortenSerializer, self).to_representation(instance)

		rep['stack'] = [technology.name for technology in instance.stack.all()]

		return rep

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Проект
class Project(models.Model):
	name = models.CharField(max_length=50, verbose_name='Имя проекта')
	add_date = models.DateTimeField(auto_now=True, verbose_name='Дата загрузки проекта')
	stack = models.ManyToManyField(to="Technology", verbose_name='Стэк проекта')
	url = models.URLField(unique=True, verbose_name='Ссылка на проект', null=True)
	github = models.URLField(unique=True, verbose_name='Ссылка на гитхаб')
	description = models.TextField(verbose_name='Описание проекта')
	contributors = models.ManyToManyField(to='Contributor', verbose_name='Контрибьюторы')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-add_date"]
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'
		unique_together = ('url', 'github')

# Технологии, используемые в проектах
class Technology(models.Model):
	name = models.CharField(max_length=20, unique=True, verbose_name='Имя технологии')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Технология'
		verbose_name_plural = 'Технологии'

# Люди, занятые разработкой проекта помимо меня
class Contributor(models.Model):
	name = models.CharField(max_length=35, unique=True, verbose_name='Имя контрибьютора')
	link = models.URLField(unique=True, null=True, verbose_name='Ссылка на контрибьютора')
	image = models.ImageField(upload_to='contributors/', verbose_name='Аватар контрибьютора')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Контрибьютор'
		verbose_name_plural = 'Контрибьюторы'

# Описание вклада контрибьютора для каждого отдельного проекта
class Contribution(models.Model):
	contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, verbose_name='Контрибьютор')
	project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
	contribution = models.TextField(verbose_name='Описание вклада')

	def __str__(self):
		return self.contribution

	class Meta:
		verbose_name = 'Вклад'
		verbose_name_plural = 'Вклады'

# Скриншоты проекта
class Screensot(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
	screenshot = models.ImageField(upload_to='projects/', verbose_name='Скришот')

	def __str__(self):
		return self.project.name

	class Meta:
		verbose_name = 'Скришот'
		verbose_name_plural = 'Скришоты'

# Посты и любые тексты на сайте
class Post(models.Model):
	name = models.CharField(max_length=60, verbose_name='Название поста')
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь-автор')
	add_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации поста')
	post = models.TextField(verbose_name='Пост')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Пост'
		verbose_name_plural='Посты'

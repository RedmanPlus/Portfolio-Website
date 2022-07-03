# Generated by Django 4.0.5 on 2022-07-02 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, unique=True, verbose_name='Имя контрибьютора')),
                ('link', models.URLField(null=True, unique=True, verbose_name='Ссылка на контрибьютора')),
                ('image', models.ImageField(upload_to='contributors/', verbose_name='Аватар контрибьютора')),
            ],
            options={
                'verbose_name': 'Контрибьютор',
                'verbose_name_plural': 'Контрибьюторы',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя проекта')),
                ('add_date', models.DateTimeField(auto_now=True, verbose_name='Дата загрузки проекта')),
                ('url', models.URLField(null=True, unique=True, verbose_name='Ссылка на проект')),
                ('github', models.URLField(unique=True, verbose_name='Ссылка на гитхаб')),
                ('description', models.TextField(verbose_name='Описание проекта')),
                ('contributors', models.ManyToManyField(to='base.contributor', verbose_name='Контрибьюторы')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Имя технологии')),
            ],
            options={
                'verbose_name': 'Технология',
                'verbose_name_plural': 'Технологии',
            },
        ),
        migrations.CreateModel(
            name='Screensot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='projects/', verbose_name='Скришот')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Скришот',
                'verbose_name_plural': 'Скришоты',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='stack',
            field=models.ManyToManyField(to='base.technology', verbose_name='Стэк проекта'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название поста')),
                ('add_date', models.DateTimeField(auto_now=True, verbose_name='Дата публикации поста')),
                ('post', models.TextField(verbose_name='Пост')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь-автор')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.TextField(verbose_name='Описание вклада')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.contributor', verbose_name='Контрибьютор')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Вклад',
                'verbose_name_plural': 'Вклады',
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('url', 'github')},
        ),
    ]
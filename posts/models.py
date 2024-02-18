from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    text = models.TextField(max_length=400, verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    group = models.ForeignKey('Group', blank=True, null=True, on_delete=models.SET_NULL, related_name='posts')


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='ЧПУ')
    description = models.TextField(max_length=400, verbose_name='Описание')
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name='текст',
        help_text='Не стесняйся, пиши, что думаешь!'
    )
    pub_date = models.DateTimeField(
        verbose_name='дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post_set_author',
        verbose_name='автор',
        help_text='Укажите автора поста.'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        related_name='post_set_group',
        verbose_name='группа',
        blank=True,
        null=True,
        help_text='Если хотите, можете выбрать принадлежность к группе.'
    )

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text


class Group(models.Model):
    title = models.CharField(
        verbose_name='the title of the group',
        max_length=200,
        help_text='Please write a title of the group (limit 200 characters).'
    )
    slug = models.SlugField(
        verbose_name='page adress',
        max_length=200,
        unique=True,
        help_text=(
            'Please write an ending of the group\'s web adress like '
            'www.blog.ru/group/<em>your_adress</em> (limit 200 characters).'
        )
    )
    description = models.TextField(
        verbose_name='description',
        help_text='Write a description for the group here.'
    )

    class Meta:
        verbose_name = "group"
        verbose_name_plural = "groups"

    def __str__(self):
        return self.title

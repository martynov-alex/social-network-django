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
        related_name='posts',
        verbose_name='автор',
        help_text='Укажите автора поста.'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='группа',
        blank=True,
        null=True,
        help_text='Если хотите, можете выбрать принадлежность к группе.'
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text


class Group(models.Model):
    title = models.CharField(
        verbose_name='название группы',
        max_length=200,
        help_text=(
            'Пожалуйста, укажите название группы (ограничение 200 '
            'символов)'
        )
    )
    slug = models.SlugField(
        verbose_name='ссылка на группу',
        max_length=200,
        unique=True,
        help_text=(
            'Пожалуйста, укажите окончание ссылки на группу вида: '
            'www.blog.ru/group/<em>имя группы</em> (ограничение 200 символов '
            'на латинице)'
        )
    )
    description = models.TextField(
        verbose_name='описание',
        help_text='Напишите описание группы'
    )

    class Meta:
        verbose_name = "группа"
        verbose_name_plural = "группы"

    def __str__(self):
        return self.title

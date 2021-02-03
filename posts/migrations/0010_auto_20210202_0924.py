# Generated by Django 2.2.6 on 2021-02-02 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20210117_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(help_text='Укажите автора поста.', on_delete=django.db.models.deletion.CASCADE, related_name='post_set_author', to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Если хотите, можете выбрать принадлежность к группе.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_set_group', to='posts.Group', verbose_name='группа'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(help_text='Не стесняйся, пиши, что думаешь!', verbose_name='текст'),
        ),
    ]

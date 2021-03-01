from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Post, Group


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        Author = get_user_model()
        cls.author = Author.objects.create()
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-group',
            description='Описание тестовой группы'
        )
        cls.post = Post.objects.create(
            text='Тестовый текст - Тестовый текст - Тестовый текст',
            author=cls.author,
            group=cls.group
        )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        post = PostModelTest.post
        field_verboses = {
            'text': 'текст',
            'pub_date': 'дата публикации',
            'author': 'автор',
            'group': 'группа',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    post._meta.get_field(value).verbose_name, expected)

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        post = PostModelTest.post
        field_help_texts = {
            'text': 'Не стесняйся, пиши, что думаешь!',
            'author': 'Укажите автора поста.',
            'group': 'Если хотите, можете выбрать принадлежность к группе.'
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    post._meta.get_field(value).help_text, expected)

    def test_object_name_is_text_field(self):
        """__str__  post - это строчка с содержимым post.text
         ограниченная 15 символами.
        """
        post = PostModelTest.post
        expected_object_name = post.text[:15]
        self.assertEquals(expected_object_name, str(post))


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='',
            description='Описание тестовой группы'
        )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        group = GroupModelTest.group
        field_verboses = {
            'title': 'название группы',
            'slug': 'ссылка на группу',
            'description': 'описание'
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    group._meta.get_field(value).verbose_name, expected)

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        group = GroupModelTest.group
        field_help_texts = {
            'title': 'Пожалуйста, укажите название группы (ограничение 200 '
                     'символов)',
            'slug': 'Пожалуйста, укажите окончание ссылки на группу вида: '
                    'www.blog.ru/group/<em>имя группы</em> (ограничение 200 '
                    'символов на латинице)',
            'description': 'Напишите описание группы'
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    group._meta.get_field(value).help_text, expected)

    def test_slug(self):
        """работает slugify для slug."""
        group = GroupModelTest.group
        slug = group.slug
        self.assertEquals(slug, 'testovaya-gruppa')

    def test_object_name_is_title_field(self):
        """__str__  group - это строчка с содержимым group.title"""
        group = GroupModelTest.group
        expected_object_name = group.title
        self.assertEquals(expected_object_name, str(group))

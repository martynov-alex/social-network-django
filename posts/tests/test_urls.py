from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from posts.models import Post, Group

User = get_user_model()


class StaticURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_homepage(self):
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)


class PostsURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Group.objects.create(
            title='Тестовый заголовок',
            slug='test-slug',
            description='Тестовое описание',
        )

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='TestUser')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_urls_exists_at_desired_location_for_guests_clients(self):
        """Страницы из списка доступны любому пользователю."""
        url_names = [
            '/',
            '/group/test-slug/',
        ]
        for url in url_names:
            with self.subTest():
                response = self.guest_client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_urls_exists_at_desired_location_for_authorized_clients(self):
        """Страницы из списка доступны авторизованному пользователю."""
        url_names = [
            '/new/',
        ]
        for url in url_names:
            with self.subTest():
                response = self.authorized_client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_urls_redirect_anonymous_on_admin_login(self):
        """Страницы из списка перенаправит анонимного пользователя на
        страницу логина.
        """
        url_names = {
            '/new/': '/auth/login/?next=/new/',
        }
        for url, redirect_url in url_names.items():
            with self.subTest():
                response = self.guest_client.get(url, follow=True)
                self.assertRedirects(response, redirect_url)

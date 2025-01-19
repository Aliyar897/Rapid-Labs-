from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser

class ApiTests(APITestCase):

    def setUp(self):
        # Create a user with each role (admin, manager, user)
        self.admin_user = CustomUser.objects.create_user(
            username='admin_username',
            password='admin_password',
            role='admin'
        )
        self.manager_user = CustomUser.objects.create_user(
            username='manager_username',
            password='manager_password',
            role='manager'
        )
        self.regular_user = CustomUser.objects.create_user(
            username='aliyar',
            password='12345',
            role='user'
        )
        
        # Generate JWT tokens for the users
        self.admin_token = str(RefreshToken.for_user(self.admin_user).access_token)
        self.manager_token = str(RefreshToken.for_user(self.manager_user).access_token)
        self.user_token = str(RefreshToken.for_user(self.regular_user).access_token)
        
    def test_admin_endpoint(self):
        url = reverse('admin')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_manager_endpoint(self):
        url = reverse('manager')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.manager_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_endpoint(self):
        url = reverse('user')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_access(self):
        url = reverse('manager')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



from http import HTTPStatus
from typing import List

from django.db import models
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from main.models import Tag, Task, User


class TestPerm(APITestCase):
    client: APIClient = None
    admin: User
    user: User
    models: list = [Tag, Task]

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.admin = User.objects.create_superuser("admin", email=None, password=None)
        cls.user = User.objects.create_user("user")
        cls.client = APIClient()

    def assert_methods_status(self, method: str, response_status: int) -> None:
        for model in self.models:
            obj = model.objects.create()
            url = reverse(f"{model._meta.model_name}s-detail", args=(obj.id,))

        response = self.client.__getattribute__(method)(url)
        assert response.status_code == response_status

    def test_isauth_perm_with_noauth_user(self) -> None:
        self.assert_methods_status("get", HTTPStatus.UNAUTHORIZED)

    def test_isauth_perm_with_auth_user(self) -> None:
        self.client.force_authenticate(user=self.user, token=None)
        self.assert_methods_status("get", HTTPStatus.OK)

    def test_isstaffdelete_perm_with_usual_user(self) -> None:
        self.client.force_authenticate(user=self.user, token=None)
        self.assert_methods_status("get", HTTPStatus.OK)
        self.assert_methods_status("delete", HTTPStatus.FORBIDDEN)

    def test_isstaffdelete_perm_with_admin(self) -> None:
        self.client.force_authenticate(user=self.admin, token=None)
        self.assert_methods_status("delete", HTTPStatus.NO_CONTENT)

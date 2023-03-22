from http import HTTPStatus
from typing import Union, List

from rest_framework.test import APIClient, APITestCase
from rest_framework.response import Response
from django.urls import reverse

from main.models import User


class TestViewSetBase(APITestCase):
    user: User = None
    client: APIClient = None
    basename: str
    task_attributes: dict

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.admin = cls.create_superuser()
        cls.user = cls.create_api_user()
        cls.client = APIClient()

    @staticmethod
    def create_api_user():
        return User.objects.create()

    @staticmethod
    def create_superuser():
        return User.objects.create_superuser('admin')

    @classmethod
    def detail_url(cls, key: Union[int, str]) -> str:
        return reverse(f"{cls.basename}-detail", args=[key])

    @classmethod
    def list_url(cls, args: List[Union[str, int]] = None) -> str:
        return reverse(f"{cls.basename}-list", args=args)

    def list(self, args: List[Union[str, int]] = None, kwargs: dict = None) -> dict:
        self.client.force_login(self.user)
        response = self.client.get(self.list_url(args), kwargs)
        assert response.status_code == HTTPStatus.OK
        return response.json()

    def create(self, data: dict, args: List[Union[str, int]] = None) -> dict:
        self.client.force_login(self.user)
        response = self.client.post(self.list_url(args), data=data, format='json')
        assert response.status_code == HTTPStatus.CREATED, response.content
        return response.data

    def retrieve(self, key: Union[str, int] = None) -> dict:
        self.client.force_login(self.user)
        response = self.client.get(self.detail_url(key))
        assert response.status_code == HTTPStatus.OK
        return response.data

    def update(self, data: dict, key: Union[str, int] = None) -> dict:
        self.client.force_login(self.user)
        response = self.client.patch(self.detail_url(key), data=data, format='json')
        assert response.status_code == HTTPStatus.OK
        return response.data

    def delete(self, key: Union[str, int] = None) -> HTTPStatus:
        self.client.force_login(self.admin)
        response = self.client.delete(self.detail_url(key))
        return response.status_code




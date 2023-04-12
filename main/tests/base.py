from http import HTTPStatus
from typing import Union, List, Optional

import factory
from rest_framework.test import APIClient, APITestCase
from rest_framework.response import Response
from django.urls import reverse

from main.models import User
from factories import TagFactory, TaskFactory, UserFactory


class ActionClient:
    def __init__(self, api_client: APIClient) -> None:
        self.api_client = api_client
        self.user: Optional[User] = None

    def init_user(self) -> None:
        self.user = User.objects.create(username="api_user")
        self.api_client.force_authenticate(user=self.user, token=None)

    def request_create_task(self, attributes) -> Response:
        task_attributes: dict = factory.build(dict, FACTORY_CLASS=TaskFactory)
        for attribute, value in attributes.items():
            task_attributes[attribute] = value

        task_attributes["author"].pop("avatar_picture", None)
        task_attributes["executor"].pop("avatar_picture", None)
        task_attributes["tags"].clear()
        url = reverse("tasks-list")
        return self.api_client.post(url, data=task_attributes, format="json")

    def create_task(self, **attributes) -> dict:
        response = self.request_create_task(attributes)
        assert response.status_code == HTTPStatus.CREATED, response.content
        return response.data

    def request_create_user(self) -> Response:
        attributes = factory.build(dict, FACTORY_CLASS=UserFactory)
        url = reverse("users-list")
        return self.api_client.post(url, data=attributes)

    def create_user(self) -> dict:
        response = self.request_create_user()
        assert response.status_code == HTTPStatus.CREATED, response.content
        return response.data

    def request_create_tag(self) -> Response:
        attributes = factory.build(dict, FACTORY_CLASS=TagFactory)
        url = reverse("tags-list")
        return self.api_client.post(url, data=attributes)

    def create_tag(self) -> dict:
        response = self.request_create_tag()
        assert response.status_code == HTTPStatus.CREATED, response.content
        return response.data


class TestViewSetBase(APITestCase):
    action_client: Optional[ActionClient] = None
    user: User = None
    client: APIClient = None
    basename: str

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.admin = cls.create_superuser()
        cls.user = cls.create_api_user()
        cls.client = APIClient()
        cls.action_client = ActionClient(cls.client)
        cls.action_client.init_user()

    @staticmethod
    def create_api_user():
        return User.objects.create()

    @staticmethod
    def create_superuser():
        return User.objects.create_superuser("admin")

    @classmethod
    def detail_url(
        cls, key: Union[str, int], args: List[Union[str, int]] = None
    ) -> str:
        if not args:
            return reverse(f"{cls.basename}-detail", args=[key])
        return reverse(f"{cls.basename}-detail", args=[key, *args])

    @classmethod
    def list_url(cls, args: List[Union[str, int]] = None) -> str:
        return reverse(f"{cls.basename}-list", args=args)

    def list(self, args: List[Union[str, int]] = None, kwargs: dict = None) -> dict:
        self.client.force_authenticate(user=self.user, token=None)
        response = self.client.get(self.list_url(args), kwargs)
        assert response.status_code == HTTPStatus.OK
        return response.json()

    def create(
        self,
        data: dict,
        args: List[Union[str, int]] = None,
        formatting: Optional[str] = None,
    ) -> dict:
        response = self.request_create(data=data, args=args, formatting=formatting)
        assert response.status_code == HTTPStatus.CREATED, response.content
        return response.data

    def request_create(
        self,
        data: dict,
        args: List[Union[str, int]] = None,
        formatting: Optional[str] = None,
    ) -> Response:
        self.client.force_authenticate(user=self.user, token=None)
        response = self.client.post(self.list_url(args), data=data, format=formatting)
        return response

    def request_retrieve(
        self, key: Union[str, int] = None, args: List[Union[str, int]] = None
    ) -> Response:
        self.client.force_authenticate(user=self.user, token=None)
        return self.client.get(self.detail_url(key, args))

    def retrieve(
        self, key: Union[str, int] = None, args: List[Union[str, int]] = None
    ) -> dict:
        response = self.request_retrieve(key, args)
        assert response.status_code == HTTPStatus.OK
        return response.data

    def update(
        self, data: dict, key: Union[str, int] = None, formatting: Optional[str] = None
    ) -> dict:
        self.client.force_authenticate(user=self.user, token=None)
        response = self.client.patch(self.detail_url(key), data=data, format=formatting)
        assert response.status_code == HTTPStatus.OK
        return response.data

    def delete(self, key: Union[str, int] = None) -> HTTPStatus:
        self.client.force_authenticate(user=self.admin, token=None)
        response = self.client.delete(self.detail_url(key))
        return response.status_code

    def request_single_resource(self, data: dict = None) -> Response:
        self.client.force_authenticate(user=self.user, token=None)
        return self.client.get(self.list_url(), data=data)

    def single_resource(self, data: dict = None) -> dict:
        response = self.request_single_resource(data)
        assert response.status_code == HTTPStatus.OK
        return response.data

    def request_patch_single_resource(self, attributes: dict) -> Response:
        self.client.force_authenticate(user=self.user, token=None)
        url = self.list_url()
        return self.client.patch(url, data=attributes)

    def patch_single_resource(self, attributes: dict) -> dict:
        response = self.request_patch_single_resource(attributes)
        assert response.status_code == HTTPStatus.OK, response.content
        return response.data

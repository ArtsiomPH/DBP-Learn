from http import HTTPStatus

from base import TestViewSetBase


class TestUserTasksViewSet(TestViewSetBase):
    basename = "user_tasks"

    def test_list(self) -> None:
        user = self.action_client.create_user()
        task1 = self.action_client.create_task(executor=user)
        self.action_client.create_task()
        tasks = self.list(args=[user["id"]])
        assert tasks == [task1]

    def test_retrieve_foreign_task(self) -> None:
        user = self.action_client.create_user()
        task = self.action_client.create_task()
        response = self.request_retrieve(user["id"], args=[task["id"]])

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_retrieve(self) -> None:
        user = self.action_client.create_user()
        created_task = self.action_client.create_task(executor=user)

        retrieved_task = self.retrieve(user["id"], args=[created_task["id"]])

        assert created_task == retrieved_task

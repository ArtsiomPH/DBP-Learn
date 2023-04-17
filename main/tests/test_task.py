from main.tests.base import TestViewSetBase


class TestTaskViewSet(TestViewSetBase):
    basename = "tasks"
    task_attributes = {
        "title": "task",
        "description": "little task",
        "creation_date": "2023-03-08",
        "mod_date": "2023-03-08",
        "deadline": "2023-03-15",
        "status": "new_task",
        "priority": 1,
        "author": {
            "username": "johnsmith",
            "first_name": "John",
            "last_name": "Smith",
            "email": "john@test.com",
            "date_of_birth": "2000-01-01",
            "phone": "+79000000000",
            "role": "developer",
        },
        "executor": {
            "username": "johnsmith",
            "first_name": "John",
            "last_name": "Smith",
            "email": "john@test.com",
            "date_of_birth": "2000-01-01",
            "phone": "+79000000000",
            "role": "developer",
        },
        "tags": [{"title": "ok"}],
    }
    task_attributes_additional = {
        "title": "another task",
        "description": "big task",
        "creation_date": "2023-04-08",
        "mod_date": "2023-04-08",
        "deadline": "2023-04-15",
        "status": "new_task",
        "priority": 1,
        "author": {
            "username": "johnsmith",
            "first_name": "John",
            "last_name": "Smith",
            "email": "john@test.com",
            "date_of_birth": "2000-01-01",
            "phone": "+79000000000",
            "role": "developer",
        },
        "executor": {
            "username": "johndorian",
            "first_name": "John",
            "last_name": "Dorian",
            "email": "john@test.ru",
            "date_of_birth": "2000-05-20",
            "phone": "+79000000000",
            "role": "developer",
        },
        "tags": [{"title": "important"}],
    }
    for_update_executor = {
        "executor": {
            "username": "christurk",
            "first_name": "Christopher",
            "last_name": "Turk",
            "email": "chris@test.com",
            "date_of_birth": "2000-01-01",
            "phone": "+79000000000",
            "role": "developer",
        }
    }

    @staticmethod
    def expected_details(entity: dict, attributes: dict) -> dict:
        attributes["author"] = {"id": entity["author"]["id"], **attributes["author"]}
        attributes["executor"] = {
            "id": entity["executor"]["id"],
            **attributes["executor"],
        }
        attributes["tags"] = entity["tags"]
        return {"id": entity["id"], **attributes}

    def test_list(self) -> None:
        task_1 = self.create(self.task_attributes, formatting="json")
        task_2 = self.create(self.task_attributes_additional, formatting="json")
        tasks_list = self.list()
        assert [task_1, task_2] == tasks_list

    def test_create(self) -> None:
        task = self.create(self.task_attributes, formatting="json")
        expected_response = self.expected_details(task, self.task_attributes)
        task["author"] = dict(task["author"])
        task["executor"] = dict(task["executor"])
        del task["author"]["avatar_picture"]
        del task["executor"]["avatar_picture"]
        assert task == expected_response

    def test_retrieve(self) -> None:
        task = self.create(self.task_attributes, formatting="json")
        retrived_user = self.retrieve(task["id"])
        assert task == retrived_user

    def test_update(self) -> None:
        for_update = {"mod_date": "2023-03-13"}
        task = self.create(self.task_attributes, formatting="json")
        updated_task = self.update(for_update, task["id"], formatting="json")
        task.update(for_update)
        assert task == updated_task
        updated_task = self.update(
            self.for_update_executor, task["id"], formatting="json"
        )
        task.update(self.for_update_executor)
        assert task == self.expected_details(updated_task, task)

    def test_delete(self) -> None:
        task = self.create(self.task_attributes, formatting="json")
        deleted_task = self.delete(task["id"])
        assert deleted_task == 204

    def test_filtration(self) -> None:
        task_1 = self.create(self.task_attributes, formatting="json")
        task_2 = self.create(self.task_attributes_additional, formatting="json")
        tasks_list = self.list(kwargs={"author": "john"})
        assert [task_2, task_1] == tasks_list
        tasks_list = self.list(kwargs={"executor": "dorian"})
        assert [task_2] == tasks_list
        tasks_list = self.list(kwargs={"tags": "ok"})
        assert [task_1] == tasks_list

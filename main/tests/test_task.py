from main.tests.base import TestViewSetBase


class TestTaskViewSet(TestViewSetBase):
    basename = "tasks"
    task_attributes = {
        'title': "task",
        "description": "little task",
        "creation_date": "2023-03-08",
        "mod_date": "2023-03-08",
        "deadline": "2023-03-15",
        "status": "new_task",
        "priority": 1,
        "author": {
            'username': 'johnsmith',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john@test.com',
            'date_of_birth': '2000-01-01',
            'phone': '+79000000000',
            'role': 'developer'
        },
        "executor": {
            'username': 'johndorian',
            'first_name': 'John',
            'last_name': 'Dorian',
            'email': 'john@test.ru',
            'date_of_birth': '2000-05-20',
            'phone': '+79000000000',
            'role': 'developer'
        },
        "tags": [
            {'title': 'ok'},
            {'title': 'not ok'}
        ]
    }
    for_update_executor = {"executor": {
            'username': 'christurk',
            'first_name': 'Christopher',
            'last_name': 'Turk',
            'email': 'chris@test.com',
            'date_of_birth': '2000-01-01',
            'phone': '+79000000000',
            'role': 'developer'
    }}

    @staticmethod
    def expected_details(entity: dict, attributes: dict):
        attributes['author'] = {"id": entity["author"]["id"], **attributes['author']}
        attributes['executor'] = {"id": entity["executor"]["id"], **attributes['executor']}
        attributes['tags'] = entity['tags']
        return {"id": entity["id"], **attributes}

    def test_create(self):
        task = self.create(self.task_attributes)
        expected_response = self.expected_details(task, self.task_attributes)
        assert task == expected_response

    def test_retrieve(self):
        task = self.create(self.task_attributes)
        retrived_user = self.retrieve(task['id'])
        assert task == retrived_user

    def test_update(self):
        for_update = {'mod_date': '2023-03-13'}
        task = self.create(self.task_attributes)
        updated_task = self.update(for_update, task['id'])
        task.update(for_update)
        assert task == updated_task
        updated_task = self.update(self.for_update_executor, task['id'])
        task.update(self.for_update_executor)
        assert task == self.expected_details(updated_task, task)

    def test_delete(self):
        task = self.create(self.task_attributes)
        deleted_task = self.delete(task['id'])
        assert deleted_task == 204

    def test_filtration(self):
        task = self.create(self.task_attributes)
        expected_tasks = self.list(kwargs={'author': 'john'})
        assert task == expected_tasks[0]
        expected_tasks = self.list(kwargs={'executor': 'dorian'})
        assert task == expected_tasks[0]
        expected_tasks = self.list(kwargs={'tags': 'ok'})
        assert task == expected_tasks[0]

from main.tests.base import TestViewSetBase


class TestTaskViewSet(TestViewSetBase):
    basename = "tasks"
    user_attributes = {
            'username': 'johnsmith',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john@test.com',
            'date_of_birth': '2000-01-01',
            'phone': '+79000000000',
            'role': 'developer'
        }
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
            'username': 'johnsmith',
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john@test.com',
            'date_of_birth': '2000-01-01',
            'phone': '+79000000000',
            'role': 'developer'
        },
        "tags": [
            {'title': 'ok'},
            {'title': 'not ok'}
        ]
    }

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
        for_update_executor = {"executor": {
            'username': 'johndorian',
            'first_name': 'John',
            'last_name': 'dorian',
            'email': 'john@test.ru',
            'date_of_birth': '2000-05-20',
            'phone': '+79000000000',
            'role': 'developer'
        }}
        updated_task = self.update(for_update_executor, task['id'])
        task.update(for_update_executor)
        assert task == updated_task


    # def test_delete(self):
    #     user = self.create(self.task_attributes)
    #     deleted_user = self.delete(user['id'])
    #     assert deleted_user == 204

    # def test_filtration(self):
    #     user = self.create(self.task_attributes)
    #     expected_users = self.list(kwargs={'username': 'john'})
    #     assert user == expected_users[0]
    #     expected_users = self.list(kwargs={'username': 'alex'})
    #     assert len(expected_users) == 0

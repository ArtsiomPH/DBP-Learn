from main.tests.base import TestViewSetBase


class TestUserViewSet(TestViewSetBase):
    basename = "users"
    user_attributes = {
        "username": "johnsmith",
        "first_name": "John",
        "last_name": "Smith",
        "email": "john@test.com",
        "date_of_birth": "2000-01-01",
        "phone": "+79000000000",
        "role": "developer",
    }

    @staticmethod
    def expected_details(entity: dict, attributes: dict) -> dict:
        return {"id": entity["id"], **attributes}

    def test_create(self) -> None:
        user = self.create(self.user_attributes)
        expected_response = self.expected_details(user, self.user_attributes)
        assert user == expected_response

    def test_retrieve(self) -> None:
        user = self.create(self.user_attributes)
        retrived_user = self.retrieve(user["id"])
        assert user == retrived_user

    def test_update(self) -> None:
        for_update = {"email": "john@test.ru"}
        user = self.create(self.user_attributes)
        updated_user = self.update(for_update, user["id"])
        user.update(for_update)
        assert user == updated_user

    def test_delete(self) -> None:
        user = self.create(self.user_attributes)
        deleted_user = self.delete(user["id"])
        assert deleted_user == 204

    def test_filtration(self) -> None:
        user = self.create(self.user_attributes)
        expected_users = self.list(kwargs={"username": "john"})
        assert user == expected_users[0]
        expected_users = self.list(kwargs={"username": "alex"})
        assert len(expected_users) == 0

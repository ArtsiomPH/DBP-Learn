from main.tests.base import TestViewSetBase


class TestTagViewSet(TestViewSetBase):
    basename = "tags"
    tag_attributes = {"title": "test"}
    tag_attributes_additional = {"title": "test_2"}

    @staticmethod
    def expected_details(entity: dict, attributes: dict) -> dict:
        return {"id": entity["id"], **attributes}

    def test_create(self) -> None:
        tag = self.create(self.tag_attributes)
        expected_response = self.expected_details(tag, self.tag_attributes)
        assert tag == expected_response

    def test_list(self) -> None:
        tag_1 = self.create(self.tag_attributes)
        tag_2 = self.create(self.tag_attributes_additional)
        tags_list = self.list()
        assert len(tags_list) == 2
        assert tag_1 in tags_list and tag_2 in tags_list

    def test_retrieve(self) -> None:
        tag = self.create(self.tag_attributes)
        retrived_tag = self.retrieve(tag["id"])
        assert tag == retrived_tag

    def test_update(self) -> None:
        for_update = {"title": "warning"}
        tag = self.create(self.tag_attributes)
        updated_tag = self.update(for_update, tag["id"])
        tag.update(for_update)
        assert tag == updated_tag

    def test_delete(self) -> None:
        tag = self.create(self.tag_attributes)
        deleted_tag = self.delete(tag["id"])
        assert deleted_tag == 204

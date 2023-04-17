from main.models import Task
from base import TestViewSetBase


class TestUserTasksViewSet(TestViewSetBase):
    basename = "task_tags"

    def add_tags(self, task: dict, tags: list) -> None:
        task_instance = Task.objects.get(pk=task["id"])
        for tag in tags:
            task_instance.tags.add(tag["id"])
        task_instance.save()

    def test_list(self) -> None:
        task = self.action_client.create_task()
        tag1 = self.action_client.create_tag()
        tag2 = self.action_client.create_tag()
        self.add_tags(task, [tag1, tag2])

        tags = self.list(args=[task["id"]])
        assert tags == [tag1, tag2]

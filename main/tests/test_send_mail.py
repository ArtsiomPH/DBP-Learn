from unittest.mock import patch, MagicMock

from django.core import mail
from django.template.loader import render_to_string

from main.models import Task
from main.services.mail import send_assign_notification
from base import TestViewSetBase


class TestSendEmail(TestViewSetBase):
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

    @patch.object(mail, "send_mail")
    def test_send_assign_notification(self, fake_sender: MagicMock) -> None:
        task = self.create(self.task_attributes)
        executor_email = task["executor"]["email"]

        send_assign_notification(task["id"])

        fake_sender.assert_called_once_with(
            subject="You've assigned a task.",
            message="",
            from_email=None,
            recipient_list=[executor_email],
            html_message=render_to_string(
                "emails/notification.html",
                context={
                    "task": Task.objects.get(pk=task["id"]),
                    "title": "New task",
                    "invite": task["executor"],
                    "inviter_name": task["executor"]["username"],
                },
            ),
        )

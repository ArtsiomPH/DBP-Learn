import io
import time

from django.core import mail
from django.template.loader import render_to_string

from celery import shared_task
from .celery import app

from main.models import Task
from main.services.storage_backends import save_file, local_file_name


@shared_task()
def send_assign_notification(task_id: int) -> None:
    task = Task.objects.get(pk=task_id)
    assignee = task.executor
    send_html_email(
        subject="You've assigned a task.",
        template="notification.html",
        context={
            "task": task,
            "title": "New task",
            "invite": assignee,
            "inviter_name": task.author.username,
        },
        recipients=[assignee.email],
    )


@shared_task()
def send_html_email(
    subject: str, template: str, context: dict, recipients: list[str]
) -> None:
    html_message = render_to_string(f"emails/{template}", context)
    return mail.send_mail(
        subject=subject,
        message="",
        from_email=None,
        recipient_list=recipients,
        html_message=html_message,
    )


@app.task
def countdown(seconds: int) -> str:
    time.sleep(seconds)
    result_data = io.BytesIO(b"test data")
    file_name = local_file_name("test_report", countdown.request, "data")
    return save_file(file_name, result_data)

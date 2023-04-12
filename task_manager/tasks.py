from django.core import mail
from django.template.loader import render_to_string

from celery import shared_task

from main.models import Task


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
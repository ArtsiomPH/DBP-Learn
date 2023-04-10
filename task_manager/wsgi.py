"""
WSGI config for task_manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from .settings import BASE_DIR

from django.core.wsgi import get_wsgi_application
import newrelic.agent

newrelic.agent.initialize(os.path.join(BASE_DIR, "newrelic.ini"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")

application = get_wsgi_application()

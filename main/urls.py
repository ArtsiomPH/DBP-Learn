from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import TaskViewSet, UserViewSet, TagViewSet

router = SimpleRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"tags", TagViewSet, basename="tags")

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]

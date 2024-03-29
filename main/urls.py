from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    TaskViewSet,
    UserViewSet,
    TagViewSet,
    CurrentUserViewSet,
    UserTasksViewSet,
    TaskTagsViewSet,
    CountdownJobViewSet,
    AsyncJobViewSet,
)
from .services.single_resource import BulkRouter

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = BulkRouter()
users = router.register(r"users", UserViewSet, basename="users")
tasks = router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"tags", TagViewSet, basename="tags")
router.register(r"current-user", CurrentUserViewSet, basename="current_user")
users.register(
    r"tasks",
    UserTasksViewSet,
    basename="user_tasks",
    parents_query_lookups=["executor_id"],
)
tasks.register(
    r"tags",
    TaskTagsViewSet,
    basename="task_tags",
    parents_query_lookups=["task_id"],
)
router.register(r"countdown", CountdownJobViewSet, basename="countdown")
router.register(r"jobs", AsyncJobViewSet, basename="jobs")

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]

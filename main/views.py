import django_filters
from rest_framework import viewsets

from .models import Tag, Task, User
from .serializers import TagSerializer, TaskSerializer, UserSerializer


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ("username",)


class TaskFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(
        field_name="author__username", lookup_expr="icontains"
    )
    executor = django_filters.CharFilter(
        field_name="executor__username", lookup_expr="icontains"
    )
    tag = django_filters.AllValuesMultipleFilter(field_name="tag__title")

    class Meta:
        model = Task
        fields = ("status", "author", "executor", "tag")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    filterset_class = UserFilter


class TaskViewSet(viewsets.ModelViewSet):
    queryset = (
        Task.objects.select_related("author")
        .select_related("executor")
        .prefetch_related("tag")
        .all()
    )
    serializer_class = TaskSerializer
    filterset_class = TaskFilter


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

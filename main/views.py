from rest_framework import viewsets

from models import Tag, Task, User
from serializers import TagSerializer, TaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('author').select_relared('executor').all()
    serializer_class = TaskSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.prefetch_related('task').all()
    serializer_class = TagSerializer

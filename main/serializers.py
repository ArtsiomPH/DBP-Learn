from rest_framework import serializers
from .models import User, Task, Tag


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone",
            "role"
        )


class TaskSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(many=True)
    author = UserSerializer()
    executor = UserSerializer()

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "creation_date",
            "mod_date",
            "deadline",
            "status",
            "priority",
            "author",
            "executor",
            "tag"
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")

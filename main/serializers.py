from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin

from .models import User, Task, Tag


class UserSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
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
            "role",
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")


class TaskSerializer(WritableNestedModelSerializer):
    author = UserSerializer(many=False)
    executor = UserSerializer(many=False)
    tags = TagSerializer(many=True)

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
            "tags",
        )

    def create(self, validated_data):
        for user in ["author", "executor"]:
            user_dict = validated_data.pop(user)
            user_instance, _ = User.objects.get_or_create(**user_dict)
            validated_data[user] = user_instance

        tags_list = []
        for tag in validated_data.pop("tags"):
            tag, _ = Tag.objects.get_or_create(**tag)
            tags_list.append(tag)

        new_task = Task.objects.create(**validated_data)
        new_task.tags.set(tags_list)
        return new_task

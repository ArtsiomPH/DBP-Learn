import factory
from factory import Factory, Faker

from main.models import Task
from .tag import TagFactory
from .user import UserFactory


class TaskFactory(Factory):
    title = Faker("color")
    description = Faker("sentence")
    creation_date = Faker("date")
    mod_date = Faker("date")
    deadline = Faker("date")
    status = Faker("random_element", elements=Task.Status.values)
    priority = Faker("pyint")
    author = factory.build(dict, FACTORY_CLASS=UserFactory)
    executor = factory.build(dict, FACTORY_CLASS=UserFactory)
    tags = [factory.build(dict, FACTORY_CLASS=TagFactory)]

    class Meta:
        model = Task

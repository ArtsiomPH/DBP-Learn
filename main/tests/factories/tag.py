from factory import Factory, Faker

from main.models import Tag


class TagFactory(Factory):
    title = Faker("sentence")

    class Meta:
        model = Tag

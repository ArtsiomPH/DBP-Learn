from factory import Factory, Faker

from main.models import User
from .base import ImageFileProvider, PhoneNumberProvider


Faker.add_provider(ImageFileProvider)
Faker.add_provider(PhoneNumberProvider)


class UserFactory(Factory):
    username = Faker("user_name")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")
    date_of_birth = Faker("date_of_birth")
    phone = Faker("fake_phone_number")
    role = Faker("random_element", elements=User.Roles.values)
    avatar_picture = Faker("image_file", fmt="jpeg")

    class Meta:
        model = User

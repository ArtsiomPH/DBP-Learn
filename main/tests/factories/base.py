from django.core.files.uploadedfile import SimpleUploadedFile
from faker.providers import BaseProvider


class ImageFileProvider(BaseProvider):
    def image_file(self, fmt: str = "jpeg") -> SimpleUploadedFile:
        return SimpleUploadedFile(
            self.generator.file_name(extension=fmt),
            self.generator.image(image_format=fmt),
        )


class PhoneNumberProvider(BaseProvider):
    def fake_phone_number(self) -> str:
        return f"{self.generator.phone_number()}"[:20]

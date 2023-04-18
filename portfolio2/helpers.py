from PIL import Image
from io import BytesIO
import os

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile


def resize_and_convert_to_webp(image):
    img = Image.open(image)
    img = img.resize((500, 700), resample=Image.LANCZOS)
    buffer = BytesIO()
    img.save(buffer, format='WEBP')
    buffer.seek(0)
    return InMemoryUploadedFile(buffer, None, f"{os.path.splitext(image.name)[0]}.webp",
                                'image/webp', buffer.getbuffer().nbytes, None)

class ResizedImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        self.width = kwargs.pop('width', 500)
        self.height = kwargs.pop('height', 900)
        super().__init__(*args, **kwargs)

    def _save_image(self, image, filename):
        webp_image = resize_and_convert_to_webp(image)
        super()._save_image(webp_image, filename)

    def pre_save(self, model_instance, add):
        file = super().pre_save(model_instance, add)
        if file and hasattr(file, 'width') and hasattr(file, 'height'):
            if file.width > self.width or file.height > self.height:
                file = resize_and_convert_to_webp(file)
        return file

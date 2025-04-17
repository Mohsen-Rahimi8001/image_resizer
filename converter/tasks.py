import time
from celery import shared_task
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from .models import Image as ImageModel

@shared_task
def resize_image(image_id, width, height):
    image = ImageModel.objects.get(id=image_id)
    original_image = Image.open(image.content)

    resized_image = original_image.resize((width, height))

    output = BytesIO()
    resized_image.save(output, format='JPEG')
    output.seek(0)
    
    time.sleep(10)
    print("slept 10 seconds to check if the task ran async.")

    image.content.save(f"resized_{image.id}.jpg", ContentFile(output.read()), save=True)

    return f"Image {image.id} resized to {width}x{height}."

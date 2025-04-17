from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return f'uploads/user_{instance.owner.id}/{filename}'


class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    content = models.ImageField(upload_to=user_directory_path)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

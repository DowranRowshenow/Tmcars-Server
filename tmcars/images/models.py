import uuid
import datetime
import os

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Image(models.Model):
    hash = models.CharField(primary_key=True, max_length=64, blank=True)
    image = models.ImageField(upload_to="products")

    class Meta:
        ordering = ["image"]

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        self.hash = uuid.uuid4()
        self.image.name = f"{datetime.datetime.now().replace(microsecond=0)}--{self.hash}.png"
        super().save(*args, **kwargs)


@receiver(pre_delete, sender=Image)
def pre_delete_story(sender, instance, **kwargs):
    path = instance.image.path

    if os.path.isfile(path):
        os.remove(path)

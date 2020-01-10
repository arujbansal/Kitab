from django.db import models
from django.conf import settings


class Book(models.Model):
    rel_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Posted By")
    image = models.ImageField(verbose_name="Image", upload_to="static/Books/img")
    title = models.CharField(max_length=256, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    price = models.IntegerField(verbose_name="Price")
    state = models.CharField(max_length=256, verbose_name="State")
    city = models.CharField(max_length=256, verbose_name="City")
    neighbourhood = models.CharField(max_length=256, verbose_name="Neighbourhood")
    phone = models.IntegerField(verbose_name="Phone Number")

    def __str__(self):
        return self.title + f" ({self.rel_user.username})"

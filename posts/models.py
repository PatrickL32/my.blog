from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Status(models.Model):
    name= models.CharField(max_length =120)
    description=models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
)
status = models.ForeignKey(
    Status,
    on_delete=models.CASCADE
)
created_on = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse("detail", args=[self.id])


# Create your models here.

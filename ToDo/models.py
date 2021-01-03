from django.db import models
# Create your models here.
from django.utils import timezone


class Todo(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task

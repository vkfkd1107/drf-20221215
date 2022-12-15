from django.db import models


class Todo(models.Model):
    title = models.CharField(blank=True, max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

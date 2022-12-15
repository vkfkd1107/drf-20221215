from django.db import models


class Post(models.Model):
    title = models.CharField(blank=True, max_length=120)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
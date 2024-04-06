from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    desc = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="Pending")
    created_at = models.DateTimeField(auto_now=True)

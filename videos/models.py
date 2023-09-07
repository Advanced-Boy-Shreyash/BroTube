from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Video(models.Model):
    """
    Video
    This is a Model for Storing Videos in Database
    """
    id = models.UUIDField(
        default = uuid.uuid4,
        primary_key=True
    )
    title = models.CharField(max_length=2500)
    description = models.TextField()
    thumbnail = models.FileField()
    video = models.FileField()
    date_of_upload = models.DateTimeField()
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

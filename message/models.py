from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class RecievedMessage(models.Model):
    reciever = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    dateOfPost = models.DateTimeField(default=timezone.now)

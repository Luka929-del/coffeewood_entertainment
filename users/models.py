from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    recovery_question = models.CharField(max_length=255, blank=True, null=True)
    recovery_answer = models.CharField(max_length=255, blank=True, null=True)
    verified_email = models.EmailField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Book(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
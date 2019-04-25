from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=30, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=40, unique=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.IntegerField(default=0)
    unliked = models.IntegerField(default=0)
    total_liked = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"

    def like(self):
        self.liked += 1
        self.total_liked += 1
        self.save()

    def unlike(self):
        self.unliked += 1
        self.total_liked -= 1
        self.save()

from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self) :
        return self.title


# Create your models here.

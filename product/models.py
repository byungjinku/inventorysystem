# product/models.py
from django.db import models
from user.models import UserModel
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

default_value = timezone.now()

# Create your models here.


class Product(models.Model):
    class Meta:
        db_table = "product"

    code = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kind = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

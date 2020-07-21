from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    content = models.TextField(null=True, blank=False)
    view_counter = models.IntegerField(null=True, blank=False, default=0)

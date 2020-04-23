import uuid as uuid
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Ingredient(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    owner = models.ForeignKey(User,
                              null=False,
                              blank=False,
                              on_delete=models.SET(-1), related_name='recipe_owner')
    ingredients = models.ManyToManyField(Ingredient)


    def __str__(self):
        return self.title

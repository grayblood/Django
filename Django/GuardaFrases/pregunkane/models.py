from django.db import models

# Create your models here.
from django.db import models
from django import forms

class User(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Tag(models.Model):
    TNom = models.CharField(max_length=5)
    Desc = models.CharField(max_length=200)
    NSFW = models.BooleanField()

    def __str__(self):
        return self.TNom


class Frase(models.Model):
    FraseText = models.CharField(max_length=100)
    Dicho = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Dichopor")
    data = models.DateTimeField(auto_now_add=True)
    Tag = models.ManyToManyField(Tag,related_name="Tags")

    def __str__(self):
        return self.FraseText


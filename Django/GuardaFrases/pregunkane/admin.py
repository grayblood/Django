from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Frase, User,Tag

admin.site.register(Frase)
admin.site.register(User)
admin.site.register(Tag)
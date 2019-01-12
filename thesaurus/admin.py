from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MainCategory)
admin.site.register(models.SubCategory)
admin.site.register(models.Card)
admin.site.register(models.Tag)

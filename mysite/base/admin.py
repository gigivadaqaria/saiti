from django.contrib import admin

# Register your models here.

from .models import POST, Topic, comment

admin.site.register(POST)
admin.site.register(Topic)
admin.site.register(comment)
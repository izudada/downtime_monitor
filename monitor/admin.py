from django.contrib import admin
from .models import WebLog, Website


admin.site.register(Website)
admin.site.register(WebLog)

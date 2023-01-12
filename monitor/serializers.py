from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import  WebLog, Website


class WebsiteSerializer(serializers.ModelSerializer):
     class Meta:
        model = Website
        fields = [ 'user', 'name', 'emails', 'url', 'state', 'created_at']


class LogSerializer(serializers.ModelSerializer):
     class Meta:
        model = WebLog
        fields = [ 'web', 'web_log', 'created_at']

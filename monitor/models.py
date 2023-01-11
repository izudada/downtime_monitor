from django.db import models
from account.models import TrackingModel, User
from jsonfield import JSONField


class Website(TrackingModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="name", max_length=50, null=False)
    url = models.URLField(null=False)
    state = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class UserNotification(TrackingModel, models.Model):
    web = models.ForeignKey(Website, on_delete=models.CASCADE)
    email = models.EmailField()


class WebLog(TrackingModel, models.Model):
    web = models.ForeignKey(Website, on_delete=models.CASCADE)
    web_log = models.JSONField(null=True)
    
    def __str__(self):
        return self.web.name
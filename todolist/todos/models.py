from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.


class FeedBack(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    mood = models.CharField(max_length=250)
    reasonMood = models.CharField(max_length=250)
    date_feedback = models.CharField(max_length=250)

    def __str__(self):
        return self.mood + ' - ' + self.date_feedback

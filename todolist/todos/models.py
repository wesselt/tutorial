from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class FeedBack(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    mood = models.CharField(max_length=250)
    reasonMood = models.CharField(max_length=250)
    date_feedback = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('todos:feedback', kwargs={'pk': self.pk})

    def __str__(self):
        return self.mood + ' - ' + self.date_feedback

class FeedBackOthers(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    foreign_mood = models.CharField(max_length=250)
    foreign_reason = models.CharField(max_length=500)
    date_feedback = models.DateField(auto_now=True)

    def __str__(self):
        return self.user_feed_back


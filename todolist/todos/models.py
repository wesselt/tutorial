from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.


class FeedBack(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    mood = models.CharField(max_length=250)
    HAPPY = 5
    GLAD = 4
    MODERATE = 3
    SAD = 2
    MAD = 1
    MOOD_CHOICES = (
        (HAPPY, 'Happy!!'),
        (GLAD, 'Glad :-)'),
        (MODERATE, 'Moderate'),
        (SAD, 'Sad :-('),
        (MAD, 'Mad !!'),
    )
    mood_choices = models.IntegerField(
        choices=MOOD_CHOICES,
        default=HAPPY,

    )
    reasonMood = models.CharField(max_length=250)
    date_first = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)

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






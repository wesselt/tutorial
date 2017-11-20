from django.contrib.auth.models import User
from django import forms
from .models import FeedBack

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class FeedbackForm(forms.ModelForm):
    mood_choices = forms.ChoiceField(choices=FeedBack.MOOD_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = FeedBack
        fields = ['mood_choices', 'reasonMood']
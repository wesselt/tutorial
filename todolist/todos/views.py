from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import FeedBack
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'todolist/main.html', { "users": users })


def details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    feedback = user.feedback_set.all()
    context = {
        'feedback': feedback,
        'user': user,
    }
    return render(request, 'todolist/details.html', context)

def give_feedback(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.feedback_set.create(mood=request.POST['mood'], reasonMood=request.POST['reasonMood'], date_feedback=request.POST['date'])
    feedback = user.feedback_set.all()
    context = {
        'feedback': feedback,
        'user': user,
    }
    return render(request, 'todolist/details.html', context)

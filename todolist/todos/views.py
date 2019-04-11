from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import FeedBack
from .forms import UserForm, FeedbackForm
from django.contrib.auth.mixins import LoginRequiredMixin
from . import database_angular_gauge, last_month, area_chart



class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/todos/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'todos/main.html'


    def get_queryset(self):
        return FeedBack.objects.filter(user=self.request.user)


class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/todos/login/'
    redirect_field_name = 'redirect_to'
    model = User
    template_name = 'todos/details.html'


class FeedbackView(LoginRequiredMixin, generic.DetailView):
    login_url = '/todos/login/'
    redirect_field_name = 'redirect_to'
    model = FeedBack
    template_name = 'todos/feedback.html'


class FeedbackCreate(LoginRequiredMixin, CreateView):
    login_url = '/todos/login/'
    redirect_field_name = 'redirect_to'
    model = FeedBack

    fields = ['user', 'mood_choices', 'reasonMood']
    def get_initial(self):

        return {'user': self.request.user}


class FeedbackUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/todos/login/'
    redirect_field_name = 'redirect_to'
    model = FeedBack
    form_class = FeedbackForm

    def form_valid(self, form):
        mood_choices = self.request.POST['mood_choices']
        if mood_choices == '5':
            form.instance.mood = 'Happy !!'
        elif mood_choices == '4':
            form.instance.mood = 'Glad :-)'
        elif mood_choices == '3':
            form.instance.mood = 'Moderate'
        elif mood_choices == '2':
            form.instance.mood = 'Sad :-('
        elif mood_choices == '1':
            form.instance.mood = 'Mad !!'

        return super(FeedbackUpdate, self).form_valid(form)


class FeedbackDelete(LoginRequiredMixin, DeleteView):
    login_url = '/todos/login/'
    redirect_field_name = 'redirect_to'
    model = FeedBack
    success_url = reverse_lazy('todos:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'todos/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # return the correct user
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('todos:index')

        return render(request, self.template_name, {'form': form})


def logoutview(request):
    logout(request)
    reverse_lazy('todos:index')


class FeedbackFormView(LoginRequiredMixin, View):
    form_class = FeedbackForm
    template_name = 'todos/feedback_form.html'
    login_url = '/todos/login/'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            feedback = form.save(commit=False)

            # cleaned (normalized) data

            mood_choices = form.cleaned_data['mood_choices']
            feedback.mood_choices = mood_choices

            if mood_choices == '5':
                feedback.mood = 'Happy !!'
            elif mood_choices == '4':
                feedback.mood = 'Glad :-)'
            elif mood_choices == '3':
                feedback.mood = 'Moderate'
            elif mood_choices == '2':
                feedback.mood = 'Sad :-('
            elif mood_choices == '1':
                feedback.mood = 'Mad !!'

            feedback.user = request.user
            feedback.save()
            return redirect('todos:index')

        return render(request, self.template_name, {'form': form})


class HomeView(LoginRequiredMixin, View):
    form_class = FeedbackForm
    template_name = 'todos/main.html'
    login_url = '/todos/login/'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        output = database_angular_gauge.chart(request)
        monthly = last_month.chart(request)
        areachart = area_chart.chart(request)
        return render(request, self.template_name, {'form': form, 'output': output, 'monthly': areachart})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            feedback = form.save(commit=False)

            # cleaned (normalized) data

            mood_choices = form.cleaned_data['mood_choices']
            feedback.mood_choices = mood_choices

            if mood_choices == '5':
                feedback.mood = 'Happy !!'
            elif mood_choices == '4':
                feedback.mood = 'Glad :-)'
            elif mood_choices == '3':
                feedback.mood = 'Moderate'
            elif mood_choices == '2':
                feedback.mood = 'Sad :-('
            elif mood_choices == '1':
                feedback.mood = 'Mad !!'

            feedback.user = request.user
            feedback.save()
            return redirect('todos:index')

        return render(request, self.template_name, {'form': form})


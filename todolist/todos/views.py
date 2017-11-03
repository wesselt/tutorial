from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from .models import FeedBack
from .forms import UserForm, LoginForm


class IndexView(generic.ListView):
    template_name = 'todos/main.html'

    def get_queryset(self):
        return FeedBack.objects.all()


class DetailView(generic.DetailView):
    model = User
    template_name = 'todos/details.html'


class FeedbackView(generic.DetailView):
    model = FeedBack
    template_name = 'todos/feedback.html'


class FeedbackCreate(CreateView):
    model = FeedBack
    fields = ['mood', 'reasonMood', 'date_feedback']


class FeedbackUpdate(UpdateView):
    model = FeedBack
    fields = ['mood', 'reasonMood', 'date_feedback']


class FeedbackDelete(DeleteView):
    model = FeedBack
    success_url = reverse_lazy('todos:index')


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'todos/login_form.html'

    # display blankform (when page is being requested)
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form })


    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('todos:index')

        return render(request, self.template_name, {'form': form})



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

from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy

from . import views
from . import database_angular_gauge

app_name = 'todos'

urlpatterns = [

    # main /todos/
    url(r'^$', views.HomeView.as_view(), name='index'),

    # login /todos/login
    url(r'^login/$', login, {'template_name': 'todos/login_form.html'}),

    # logout /todos/logout
    url(r'^logout/$', logout, {'next_page': reverse_lazy('todos:index')}, name='logout'),

    # main /todos/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # details /todos/<user_id>/
    url(r'^details/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    # add user /todos/feedback/add/
    url(r'feedback/add/$', views.FeedbackFormView.as_view(), name='feedback-add'),

    # single feedback
    url(r'^feedback/(?P<pk>[0-9]+)/$', views.FeedbackView.as_view(), name='feedback'),

    # update user /todos/feedback/4/update
    url(r'feedback/(?P<pk>[0-9]+)/update/$', views.FeedbackUpdate.as_view(), name='feedback-update'),

    # update user /todos/feedback/4/delete/
    url(r'feedback/(?P<pk>[0-9]+)/delete/$', views.FeedbackDelete.as_view(), name='feedback-delete'),

    # /todos/home/
    url(r'^home/$', views.HomeView.as_view(), name='home'),

]

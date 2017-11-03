from django.conf.urls import url

from . import views

app_name = 'todos'

urlpatterns = [

    # main /todos/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # login /todos/login
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),

    # main /todos/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # details /todos/<user_id>/
    url(r'^details/(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name='details'),

    # add user /todos/feedback/add/
    url(r'feedback/add/$', views.FeedbackCreate.as_view(), name='feedback-add'),

    # single feedback
    url(r'^feedback/(?P<pk>[0-9]+)/$', views.FeedbackView.as_view(), name='feedback'),

    # update user /todos/feedback/4/update
    url(r'feedback/(?P<pk>[0-9]+)/update/$', views.FeedbackUpdate.as_view(), name='feedback-update'),

    # update user /todos/feedback/4/delete/
    url(r'feedback/(?P<pk>[0-9]+)/delete/$', views.FeedbackDelete.as_view(), name='feedback-delete'),


]

from django.conf.urls import url

from . import views

app_name = 'todos'

urlpatterns = [

    # main /todos/
    url(r'^$', views.index, name='index'),

    # details /todos/<user_id>/
    url(r'^details/(?P<user_id>[0-9]+)/$', views.details , name='details'),

    # details /todos/<user_id>/give_feedback
    url(r'^details/(?P<user_id>[0-9]+)/give_feedback/$', views.give_feedback, name='give_feedback'),

]

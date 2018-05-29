from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^[/](?P<topic_name>[\w]+)[/]$', views.topic_list, name='topic_list'),
    # url(r'^(?P<topicName>[\w]+)[/]$', views.topic_menu, name='topic_menu'),
    # url(r'^(?P<alias>[\w]+)[/]papers[/](?P<paper_nbr>[\d]+)$', views.paper, name='topic_menu'),
    # url(r'^(?P<alias>[\w]+)[/]papers[/](?P<paper_nbr>[\d]+)[/](?P<q_nbr>[\d]+)[/]$', views.paper, name='topic_menu'),
    url(r'^$', views.topic_list, name='post_list'),
    url(r'^(?P<alias>[\w]+)[/]$', views.topic_menu, name='topic_menu'),
    url(r'^(?P<alias>[\w]+)[/]papers[/]$', views.paper_list, name='topic_menu'),
    url(r'^(?P<alias>[\w]+)[/]papers[/](?P<q_nbr>[\d]+)[/]$', views.paper, name='topic_menu'),
    url(r'^(?P<alias>[\w]+)[/]tutorial$', views.tutorial1, name='topic_menu'),
    url(r'^(?P<alias>[\w]+)[/]formula', views.formula1, name='topic_menu'),
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news_list, name='news_list'),
    url(r'^post/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
]
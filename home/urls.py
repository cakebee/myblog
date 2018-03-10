from django.conf.urls import url
from . import views as home_views
urlpatterns = [
	url(r'^allpost/$', home_views.allpost, name='allpost'),
    url(r'^post/(?P<article_id>[0-9]+)/$', home_views.post, name='post'),
    url(r'^about/$', home_views.about, name='about'),
    url(r'^contact/$', home_views.contact, name='contact'),
    url(r'^$', home_views.index, name='index')
]
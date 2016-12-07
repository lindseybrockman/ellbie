from django.conf.urls import url

from resume import views


urlpatterns = [
    url(r'^$', views.index, name='resume'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url('endpoint-name-here', views.ApiNameHere.as_view()),
]

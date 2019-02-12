from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# registering our Hello api viewset with the router
# args are
# - endpoint name
# - api name inside views.py
# - base name when calling (no need when registering a Model Viewset)
router.register('hello-punk', views.Hello, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    url('endpoint-name-here', views.ApiNameHere.as_view()),
    # url endpoint is empty, since we let the router object handles it
    url('', include(router.urls))
]

from django.urls import path

from dj_elastictranscoder.views import endpoint as transcoder_endpoint

urlpatterns = (path('endpoint/', transcoder_endpoint, name='transcoder_endpoint'),)


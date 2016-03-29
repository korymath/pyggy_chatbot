from django.conf.urls import include, url
from django.contrib import admin

from django_chatterbot.api import ChatterBotView


urlpatterns = [
    url(
        r'^$',
        ChatterBotView.as_view(),
        name="chatterbot",
    ),
]
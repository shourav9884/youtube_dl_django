from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
]
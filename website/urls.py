from django.urls import path
from website.views import *


urlpatterns = [
    path('', home_view,name= 'home'),
]
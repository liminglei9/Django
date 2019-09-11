from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('index/',index),
    path('zj/',zj),
    path('cx/',cx),
    path('xg/',xg),
    path('sc/',sc),
    path('duozj/',duozj),
    path('duocx/',duocx),
    # path('duoxg/',duoxg),
    # path('duosc/',duosc),
]
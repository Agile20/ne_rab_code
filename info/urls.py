from .views import *

from django.urls import path 

urlpatterns =[
    path('registration/', SubmitApplicationView.as_view()),
]



from django.urls import path
from .views import HelloApiVeiw

urlpatterns =[
  path('hello/',HelloApiVeiw.as_view())
]
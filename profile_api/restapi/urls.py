from django.urls import path,include
from .views import HelloApiVeiw,HelloViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('helloviewset/',HelloViewSet,basename='helloviewset')

urlpatterns =[
  path('hello/',HelloApiVeiw.as_view()),
  path('',include(router.urls))
]
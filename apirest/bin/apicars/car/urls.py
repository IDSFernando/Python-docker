from django.conf.urls import url
from car import views

urlpatterns = [
    url(r'^carros/$', views.listAllCars),
    url(r'^carros/(?P<pk>[0-9]+)/$', views.getCarDataByID),
]
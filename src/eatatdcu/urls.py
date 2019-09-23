from django.urls import path

from . import views
app_name = 'eatatdcu'

#TODO add the path for the restaurants url
urlpatterns = [
   path('',views.index,name='index'),
    path('', views.restaurants,name='restaurants'),
]

from django.urls import path

from actions.action import views

app_name = 'action'
urlpatterns = [
    path('', views.home, name='home'),
]

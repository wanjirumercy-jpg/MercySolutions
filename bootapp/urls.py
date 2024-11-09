from django.urls import path
from . import views

app_name = "bootapp"

urlpatterns = [
    path('',views.index, name = 'home'),
    path('start/',views.starter, name = 'start'),
]
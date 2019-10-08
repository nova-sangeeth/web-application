from django.urls import path

#  THE PERIOD RESEMBLES THE CURREMT DIRECTORY OR THE FOLDER
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new_item)

]

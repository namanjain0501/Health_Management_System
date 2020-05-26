from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'ratings'

urlpatterns = [
    path('edit_ratings/<id>',views.edit_ratings,name="edit-ratings"),
]
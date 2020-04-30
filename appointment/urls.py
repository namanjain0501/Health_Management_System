from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'appointment'

urlpatterns = [
    path('book/<id>/', views.book_appointment,name="book-appointment"),
    path('view/',views.view_appointment,name="view-appointment"),
    path('cancel/<id>',views.cancel_view,name="cancel-appointment"),
    path('approve/<id>',views.approve_view,name="approve-appointment"),
    path('reject/<id>',views.reject_view,name="reject-appointment"),
    path('edit_cmts/<id>',views.edit_cmts,name="edit-cmts"),
]
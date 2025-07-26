# panel/admin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("sync-db/", views.trigger_sync, name="trigger_sync"),
]

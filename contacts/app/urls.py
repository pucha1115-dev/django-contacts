from django.urls import re_path as url
from app import views

urlpatterns = [
    url(r'^contacts/$', views.ContactApi),
    url(r'^contacts/([0-9]+)$', views.ContactApi)
]
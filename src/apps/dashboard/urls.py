from django.urls import include, path, re_path

from . import views

urlpatterns = [
    re_path(r'^moderator/', include('dashboard.contrib.moderator.urls')),
    re_path(r'^customer/', include('dashboard.contrib.customer.urls')),
    re_path(r'^performer/', include('dashboard.contrib.performer.urls')),
]
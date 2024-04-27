from django.urls import include, path, re_path

from . import views

urlpatterns = [
    re_path(
        r'^$', views.CustomerView.as_view(),
        name='customer'
    ),
]
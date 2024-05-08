from django.urls import include, path, re_path

from . import views

urlpatterns = [
    re_path(
        r'^$', views.ModeratorView.as_view(),
        name='moders'
    ),
    re_path(
        r'^tasks/$',
        views.ModeratorTaskView.as_view(),
        name='moderator_tasks'
    ),
]
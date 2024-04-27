from django.urls import include, path, re_path

from . import views

urlpatterns = [
    #path(
    #        'login/',
    #        views.SignInViev.as_view(),
    #        name='login'
    #    ),  
    path(
        'registration-complite/',
        views.RegistrationCompleteView.as_view(),
        name='registration_complite'
    ),
    path(
        'registration/',
        views.RegistrationView.as_view(),
        name='registration'
    ),
    path(
        'user-info/<int:pk>',
        views.UserInfoView.as_view(),
        name='user_info'
    ),
    path(
        'user-update/<int:pk>',
        views.UpdateUserView.as_view(),
        name='user_update'
    ),
    path(
        'login/',
        views.SignInViev.as_view(),
        name='login'
        ), 
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
]
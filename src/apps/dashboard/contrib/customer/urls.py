from django.urls import include, path, re_path

from . import views

urlpatterns = [
    re_path(
        r'^$', views.CustomerView.as_view(),
        name='customer'
    ),
    re_path(
        r'^tasks/$',
        views.CustomerTaskView.as_view(),
        name='customer_tasks'
    ),
    path(
        'customer-performer-tasks/<int:pk>',
        views.CustomerPerformerTaskView.as_view(),
        name='customer_performer_tasks'
    ),

    
    re_path(
        r'^performers/$',
        views.PerformerView.as_view(),
        name='customer_performers'
    ),
    path(
        'create-tasks/<int:pk>',
        views.CreateCustomerTaskView.as_view(),
        name='create_customer_tasks'
    ),
    
]
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView, RedirectView

from . import views

admin.site.site_header = "Admin panel"
admin.site.site_title = "Admin panel"
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        r'^$',
        views.HomeView.as_view(
            get_context_data=lambda: {
                'is_homepage': True,
                }
        ),
        name='home_page'
    ), 
    re_path(r'^dashboard/', include('dashboard.urls')),
    re_path('^accounts/', include('userprofiles.urls')),


    re_path(r'^500/$', TemplateView.as_view(template_name="500.html")),
    re_path(r'^503/$', TemplateView.as_view(template_name="503.html")),
    re_path(r'^404/$', TemplateView.as_view(template_name="404.html"), name='404'),
    re_path(r'^403/$', TemplateView.as_view(template_name="403.html"), name='403'),
]

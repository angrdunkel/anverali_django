from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

from django.views.generic import TemplateView, View, CreateView
from django.http.response import Http404, JsonResponse

from .mixins import ModersMixin, ModerRequiredViewMixin

from dashboard.contrib.task.views import BaseTaskView


class ModeratorView(ModerRequiredViewMixin, TemplateView, ModersMixin):
    template_name = "moderator/moderator_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(ModeratorView, self).get_context_data(**kwargs)
        context['users'] = get_user_model().objects.all().order_by('email')
        return context
    

class ModeratorTaskView(BaseTaskView):
    template_name = "customer/task.html"
    is_add = True

    def get_context_data(self, **kwargs):
        context = super(ModeratorTaskView, self).get_context_data(**kwargs)
        context['tasks'] = self.get_tasks()
        return context
    


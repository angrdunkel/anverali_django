from django.shortcuts import render

from django.views.generic import TemplateView

class PerformerView(TemplateView):
    template_name = "performer/performer_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(PerformerView, self).get_context_data(**kwargs)
        return context
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='homepage.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if 'home_page_verification' in self.request.resolver_match.view_name:
            context['verification_status'] = True
        response = self.render_to_response(context)
        return response
from django.shortcuts import render

from django.views.generic import TemplateView

class CustomerView(TemplateView):
    template_name = "customer/customer_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(CustomerView, self).get_context_data(**kwargs)
        return context
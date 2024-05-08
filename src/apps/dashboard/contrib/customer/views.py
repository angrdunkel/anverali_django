from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http.response import Http404, JsonResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

from dashboard.contrib.task.views import BaseTaskView, BaseCreateTaskView

from .mixin import CustomerMixin, CustomerRequiredViewMixin

from .forms import TaskCustomerForm

User = get_user_model()

class CustomerView(TemplateView):
    template_name = "customer/customer_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(CustomerView, self).get_context_data(**kwargs)
        return context
    
class CustomerTaskView(BaseTaskView):
    template_name = "customer/task.html"

    def get_context_data(self, **kwargs):
        context = super(CustomerTaskView, self).get_context_data(**kwargs)
        context['tasks'] = self.get_tasks().filter(customer=self.request.user)
        return context
    

class CustomerPerformerTaskView(BaseTaskView):
    template_name = "customer/task.html"
    template_name_ajax = "customer/ajax/task_ajax.html"
    
    def get_context_data(self, **kwargs):
        context = super(CustomerPerformerTaskView, self).get_context_data(**kwargs)
        context['tasks'] = self.get_tasks().filter(customer=self.request.user, performer=self.get_performer_data(self.kwargs.get('pk', 0)))
        return context
    
    def get(self, request, *args, **kwargs):
            context = self.get_context_data()
            tasks = context['tasks']
            if self.is_ajax():
                data = {
                'html': render_to_string(
                    template_name=self.template_name_ajax,
                    request=request,
                    context={
                        'tasks': tasks,
                        'performer': self.get_performer_data(self.kwargs.get('pk', 0))
                    }
                    
                ),
                'label': f'Tasks: {self.get_performer_data(self.kwargs.get('pk', 0)).get_full_name()}'                
                }
                return JsonResponse(data)
            return super(CustomerPerformerTaskView, self).get(request, *args, **kwargs)
    
class PerformerView(CustomerRequiredViewMixin, TemplateView, CustomerMixin):
    template_name = "customer/performer.html"
    template_name_ajax = "customer/ajax/performer_ajax.html"


    def get_object(self):
        return self.gel_all_user_profiles().filter(user__type=3)

    def get_context_data(self, **kwargs):
        context = super(PerformerView, self).get_context_data(**kwargs)
        context['performers'] = self.get_object()
        return context
    
class CreateCustomerTaskView(BaseCreateTaskView):
    template_name = "customer/task_form.html"
    template_name_ajax = "customer/ajax/task_form_ajax.html"
    form_class = TaskCustomerForm
    success_url = reverse_lazy('customer_tasks')

    def get_performer(self):
        return User.objects.get(id=self.kwargs.get('pk', 0))
    
    def get_customer(self):
        return self.request.user
    
    def get_action_url(self, pk):
        return reverse_lazy('create_customer_tasks', kwargs={'pk': pk})
    
    def get_context_data(self, **kwargs):
        ctx = super(CreateCustomerTaskView, self).get_context_data(**kwargs)
        ctx['performer'] = self.get_performer()
        ctx['action_url'] = self.get_action_url(ctx['performer'].id)
        return ctx

    def get(self, request, *args, **kwargs):
            self.template_names = self.get_template_names()
            context = self.get_context_data()      
            self.form = context['form']   
            performer = context['performer']     

            if self.is_ajax():
                data = {
                'html': render_to_string(
                    template_name=self.template_names,
                    request=request,
                    context={
                        'form': self.form,
                        'performer': performer
                        }
                    ),
                'label': f"Create task: {performer.get_full_name()}"
                }
                return JsonResponse(data)
            return super(CreateCustomerTaskView, self).get(request, *args, **kwargs)



    

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http.response import Http404, JsonResponse
from django.views.generic import FormView
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .mixins import TaskMixin, TaskRequiredViewMixin

class BaseTaskView(TaskRequiredViewMixin, TemplateView, TaskMixin):
    template_name = None
    template_name_ajax = None
    is_add = False
    
class BaseCreateTaskView(TaskRequiredViewMixin, TaskMixin,  FormView):
    form_class = None
    template_name = None
    template_name_ajax = None
    success_url = None
    success_url_ajax = None
    success_template = "task/ajax/success_task_ajax.html"    

    def form_invalid(self, form):
        if self.is_ajax():
            data = {
                'html': render_to_string(
                    template_name=self.get_template_names(),
                    request=self.request,
                    context={
                        'form': form,
                        'performer': self.get_performer()
                    }
                ),
                    'status': False
            }
            return JsonResponse(data)
        return super(BaseCreateTaskView, self).form_invalid(form)
    
    def form_valid(self, form, **kwargs):
        new_task = form.save(performer=self.get_performer(), customer=self.get_customer())
        if self.is_ajax():
            data = {
                'html': render_to_string(
                    template_name=self.success_template,
                    context={
                        'task': new_task['task'],
                        'success_url': reverse_lazy('customer_performer_tasks', kwargs={'pk': new_task['performer'].id})
                        },
                    request=self.request
                ),
                'staus': True
            }
            return JsonResponse(data)
        
        return HttpResponseRedirect(self.success_url)
    

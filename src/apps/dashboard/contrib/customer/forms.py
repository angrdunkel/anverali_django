from django import forms
from django.utils.translation import gettext_lazy as _

from dashboard.contrib.task.models import Task, TaskRoom

class TaskCustomerForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'comment', 'is_active']

    def save(self, performer, customer, commit=True, **kwargs):
        obj = super(TaskCustomerForm, self).save(commit, **kwargs)
        task_room = TaskRoom(
            task=obj,
            customer=customer,
            performer=performer
        )
        task_room.save()

        return {
            'task': obj,
            'performer': performer,
            'customer': customer
        }
        
        
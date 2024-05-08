from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    title = models.CharField(
        _('Title'), 
        max_length=255, 
        help_text=_('Title for task')
    )
    comment = models.TextField(
        _('Comment'), 
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(
        _('Created at'), 
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Updated at'), 
        auto_now=True
    )
    complite_at = models.DateTimeField(
        _('Complite at'), 
        auto_now=True
    )
    is_active = models.BooleanField(
        _('Active'), 
        default=False
    )
    is_complite = models.BooleanField(
        _('Complite'), 
        default=False
    )

    def __str__(self):
        return self.title

class TaskRoom(models.Model):
    task = models.ForeignKey(
        Task,
        verbose_name=_('Task'),
        related_name='task_room',
        on_delete=models.CASCADE,
    )
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Customer'),
        related_name='task_customer',
        on_delete=models.CASCADE,
    )
    performer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Performer'),
        related_name='task_performer',
        on_delete=models.CASCADE,
    )

    def __str__(self):
            return self.task.title
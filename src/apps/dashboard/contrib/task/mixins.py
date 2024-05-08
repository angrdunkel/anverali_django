from userprofiles.mixins import UserProfilesMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404

from project.mixins import BaseMixin

from .models import TaskRoom
from userprofiles.models import User, UserProfile

class LoginRequiredViewMixin(LoginRequiredMixin):
    pass

class TaskRequiredViewMixin(LoginRequiredViewMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            raise Http404
        return super().dispatch(request, *args, **kwargs)
    
class TaskMixin(BaseMixin):
    def get_tasks(self):
        return TaskRoom.objects.all()
    
    def get_performer_data(self, pk):
        return User.objects.get(id=pk)
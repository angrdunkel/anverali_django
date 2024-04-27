from django.shortcuts import render
from userprofiles.mixins import UserProfilesMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404

class LoginRequiredViewMixin(LoginRequiredMixin):
    pass


class ModerRequiredViewMixin(LoginRequiredViewMixin):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and not self.request.user.is_admin():
            raise Http404
        return super().dispatch(request, *args, **kwargs)
    
class ModersMixin(UserProfilesMixin):
    pass
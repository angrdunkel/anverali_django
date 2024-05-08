from django.shortcuts import render
from userprofiles.mixins import UserProfilesMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404

from userprofiles.models import User, UserProfile

class LoginRequiredViewMixin(LoginRequiredMixin):
    pass


class CustomerRequiredViewMixin(LoginRequiredViewMixin):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and not self.request.user.is_customer():
            raise Http404
        return super().dispatch(request, *args, **kwargs)
    
class CustomerMixin(UserProfilesMixin):
    pass
    
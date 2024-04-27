from django.shortcuts import render, get_object_or_404

from django.views.generic import TemplateView, View, CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model, login as auth_login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, FileResponse
from django.http.response import Http404, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from .forms import BaseRegistrationForm, UpdateUserForm, RememberLoginForm
from .mixins import UserProfilesMixin

User = get_user_model()

def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return HttpResponseRedirect(reverse('home_page'))

class RegistrationView(CreateView, UserProfilesMixin):
    form_class = BaseRegistrationForm
    success_url = 'registration_complite'
    template_name = 'registration/registration.html'
    template_name_ajax = 'registration/ajax/registration_ajax.html'

    def get_template_names(self):
        if self.is_ajax():
            return [self.template_name_ajax]
        return [self.template_name]
    
    def get_username_prefix(self, new_user):
        if new_user.is_admin():
            return 'S10'
        elif new_user.is_customer():
            return 'C10'
        elif new_user.is_performer():
            return 'P10'
    
    def form_valid(self, form):      
        new_user = form.save(commit=False)
        self.username_prefix = self.get_username_prefix(new_user)        
        while True:
            new_username = self.generate_username()
            if not User.objects.filter(username=new_username).exists():
                new_user.username = new_username
                break
        if new_user.is_admin():
            new_user.is_staff = True
        new_user.is_active = True
        new_user.save()

        return HttpResponseRedirect(reverse('registration_complite'))

class RegistrationCompleteView(TemplateView, UserProfilesMixin):
    template_name = 'registration/registration_complete.html'
    template_name_ajax = 'registration/ajax/registration_complete_ajax.html'
    
    def get_template_names(self):
        if self.is_ajax():
            return [self.template_name_ajax]
        return [self.template_name]
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        return ctx    
    
class UserInfoView(View, UserProfilesMixin):
    template_name = 'userprofiles/ajax/user_info.html'

    def get_object(self, queryset=None):
        return get_object_or_404(
            User.objects.all(),
            id=self.kwargs.get('pk', 0)
        )

    def get(self, request, *args, **kwargs):
        self.object = self.get_object() 
        if self.is_ajax():
            data = {
                'html': render_to_string(
                    template_name=self.template_name,
                    request=request,
                    context={
                        'user': self.object
                    }
                ),
                'label': "User information"
            }
            return JsonResponse(data)
        raise Http404
    
class UpdateUserView(UpdateView, UserProfilesMixin):
    template_name = 'userprofiles/update_user.html'
    template_name_ajax = 'userprofiles/ajax/update_user_ajax.html'
    success_url = reverse_lazy('moders')
    form_class = UpdateUserForm

    def get_object(self):
        obj = get_object_or_404(
            get_user_model().objects.all(),
            id=self.kwargs.get('pk', 0)
        )
        return obj
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if self.is_ajax():
            data = {
                'html': render_to_string(
                    template_name=self.template_name_ajax,
                    request=request,
                    context={
                        'object': self.object,
                        'form': self.get_form(),
                    }
                )
            }
            return JsonResponse(data)
        return self.render_to_response(context)
    
    def form_valid(self, form):
        return super(UpdateUserView, self).form_valid(form)
    
class SignInViev(LoginView, UserProfilesMixin):
    redirect_authenticated_user = False
    form_class = RememberLoginForm
    template_name = 'registration/login.html'
    template_name_ajax = 'registration/ajax/login_ajax.html'

    def get(self, request, *args, **kwargs):
        if self.is_ajax():
            data = {
                'html': render_to_string(
                    template_name=self.template_name_ajax,
                    request=request,
                    context={
                        'form': self.get_form(),
                    }
                ),
                'label': "Sign in"
            }
            return JsonResponse(data)
        raise Http404

    def get_success_url(self):
        user = self.request.user
        if user.is_admin():
            return reverse('moders')
        elif user.is_customer():
            return reverse('customer')
        elif user.is_customer():
            return reverse('performer')
        

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        print(f'Error {self.request}')
        print(self.request.POST.get('username'))
        return self.render_to_response(self.get_context_data(form=form))
    
    def form_valid(self, form):
        auth_login(self.request, form.get_user())
                
        if self.is_ajax():
            if self.request.user.is_client:
                return JsonResponse({
                    "status": "ok",
                    "redirect_url": self.get_success_url(),
                })
        
        return HttpResponseRedirect(self.get_success_url())
    
def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return HttpResponseRedirect(reverse('home_page'))
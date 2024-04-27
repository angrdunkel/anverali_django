from random import choice

from .models import User
from project.mixins import BaseMixin

class UserProfilesMixin(BaseMixin):
    
    def get_all_users(self):
        return User.objects.all().order_by('last_name')
    
    def generate_username(self, size=8):
        allowed_chars = '0123456789'
        code = ''.join([choice(allowed_chars) for i in range(size)])
        return "".join([self.username_prefix, '-', code[0:4], '-', code[4:8]])
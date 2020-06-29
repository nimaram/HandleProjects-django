from django.db import models
from django.contrib.auth.models import AbstractBaseUser
class User(AbstractBaseUser):
    email = models.EmailField(max_length=120,unique=True)
    talents = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['talents']
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
from django.db import models
from users.models import User
class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110,unique=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

 class ProjectMembership(models.Model):

     ROLE_CHOICES = (
         ('RG' : 'Guest'),
         ('RR' : 'Reporter'),
         ('RD' : 'Developer'),
         ('RM' : 'Master'),
         ('RO' : 'Owner'),
     )

     project = models.ForeignKey(Project,on_delete=models.CASCADE)
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     role = models.CharField(max_length=4,choices=ROLE_CHOICES,default='RG',verbose_name='دسترسی')
     is_current = models.BooleanField(default=False)

     class Meta:
         # برید لینک پایین تا رستگار شوید
         # https://docs.djangoproject.com/en/3.0/ref/models/options/#unique-together
         # اگه بیش از 1 کلید خارجی دارید و میخواید اون کلیدا یونیک یا شاخص باشن از این لعنتی استفاده کنید.
         unique_together = ['user','project']
         ordering = ['project']
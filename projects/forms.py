from django import forms
from django.conf import settings
from .models import Project , ProjectMembership
class CreateProject(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['slug','owner']

class MemberShip(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(MemberShip,self).__init__(*args,**kwargs)

        self.fields['project'].queryset = Project.objects.filter(owner=user)
    class Meta:
        model = ProjectMembership
        exclude = ['is_current','project']        
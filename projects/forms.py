from django import forms
from django.conf import settings
from .models import Project , ProjectMembership
class CreateProject(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['slug','owner']

class MemberShip(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.filter(owner=settings.USER_TOCHPAD))
    class Meta:
        model = ProjectMembership
        exclude = ['is_current']        
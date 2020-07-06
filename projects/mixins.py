from django.shortcuts import render , redirect , get_object_or_404
from django.http import Http404
from .models import Project
class UserProtectMixin():
    def dispatch(self,request,*args,**kwargs):
        
        inc = get_object_or_404(Project,pk=self.kwargs['project'])
        if request.user == inc.owner:
            pass
        else:
            raise Http404("You can't access this page")
        return super().dispatch(request,*args,**kwargs)
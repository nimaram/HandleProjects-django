from django.shortcuts import render , redirect , get_object_or_404
from django.urls import reverse_lazy
from .forms import CreateProject , MemberShip
from django.conf import settings
from .models import Project
from .mixins import UserProtectMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils.text import slugify
from django.views.generic import CreateView , ListView
def home(request):
    project = ''
    if request.user.is_authenticated:
        project = Project.objects.filter(owner=request.user)
    return render(request,'site/index.html',{'projects':project})


# class home(ListView):
#     template_name = 'site/index.html'
#     model = Project
#     def get_context_data(slef,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['projects'] = Project.objects.filter(owner=self.request.user)
#         return context

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateProject(request.POST)
            if form.is_valid():
                slug = slugify(form.cleaned_data.get('name'))
                project = form.save(commit=False)
                project.slug = slug
                project.owner = request.user
                project.save()
                return redirect('project:home')
        else:
            form = CreateProject()
        return render(request,'site/create.html',{'form':form})
    else:
        return redirect('project:home')

def detail(request,slug):
    project = get_object_or_404(Project,slug=slug)
    return render(request,'site/detail.html',{'project':project})


def delete(request,slug,user_id):
    if request.user.is_authenticated:
        if request.user.id == user_id:
            if request.method == 'POST':
                Project.objects.filter(slug=slug).delete()
                return redirect('project:home')
            return render(request,'site/delete.html')
        else:
            return redirect('project:home') 
            
    else:
        return redirect('project:home')    

def edit(request,slug,user_id):
    project = get_object_or_404(Project,slug=slug)
    if request.user.is_authenticated:
        if request.user.id == user_id:
            if request.method == 'POST':
                form = CreateProject(request.POST,instance=project)
                if form.is_valid():
                    e_project = form.save(commit=False)
                    e_project.slug = slugify(form.cleaned_data.get('name'))
                    e_project.save()
                    return redirect('project:home') 
            else:
                form = CreateProject(instance=project)
            return render(request,'site/edit.html',{'form':form})
        else:
            return redirect('project:home')     

    else:
        return redirect('project:home')
# def addcont(request,slug,user_id):
#     if request.user.is_authenticated:
#         if request.user.id == user_id:
#             if request.method == 'POST':
#                 form = MemberShip(request.POST)
#                 if form.is_valid():
#                     form.save()
#                     return redirect(request.GET,'project:home')
#             else:
#                 form = MemberShip()
#             return render(request,'site/addcont.html',{'form':form})    
#         else:
#             return redirect('project:home') 
#     else:
#         return redirect('project:home')                         
# suggest ==>  CBV
# CBV ==> self.request.user 
class addcont(LoginRequiredMixin,UserProtectMixin,CreateView):
    login_url = reverse_lazy('users:login')
    form_class = MemberShip
    template_name = 'site/addcont.html'
    success_url = reverse_lazy('project:home')
    def get_form_kwargs(self):
        kwargs = super(addcont,self).get_form_kwargs()
        kwargs.update({
            'user':self.request.user.id
        })
        return kwargs


    def form_valid(self,form,**kwargs):
        project = get_object_or_404(Project,pk=self.kwargs['project'])
        member_ship = form.save(commit=False)
        member_ship.is_current = True
        member_ship.project = project
        member_ship.save()
        return super().form_valid(form)



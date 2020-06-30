from django.shortcuts import render , redirect , get_object_or_404
from .forms import CreateProject
from .models import Project
from django.utils.text import slugify
def home(request):
    project = ''
    if request.user.is_authenticated:
        project = Project.objects.filter(owner=request.user)
    return render(request,'site/index.html',{'projects':project})


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

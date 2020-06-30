from django.shortcuts import render , redirect
from .forms import CreateProject
from .models import Project
from django.utils.text import slugify
def home(request):
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

from django.shortcuts import render , redirect

def home(request):
    return render(request,'site/index.html')


def create(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('project:home')    

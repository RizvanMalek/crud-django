from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from .models import TmpModel

# Create your views here.
def home(request):
    data = TmpModel.objects.all()
    return render(request,"home.html",{"data":data})

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def profile(request):
    return HttpResponse("<h1>Profile Page</h1>")    


def create_model(request):
    if request.POST:

        if "btnUpdate" in request.POST:
            txt1 = request.POST['txt1']
            hd = request.POST['hd']
            tmp = TmpModel.objects.filter(id=hd).update(name=txt1)
            return redirect('/')
        else:
            txt1 = request.POST['txt1']
            tmp = TmpModel(name=txt1)
            tmp.save()
            return redirect('/')
    else:
        return HttpResponse("Not Get Request")


def delete_model(request,id):
    tmp = TmpModel.objects.filter(id=id).delete()
    return redirect('/')

def update(request,id):
    tmp = TmpModel.objects.get(id=id)
    return render(request,'home.html',{"user":tmp})


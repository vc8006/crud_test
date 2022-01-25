from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentReg
from .models import User

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            # fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm,email=em,password = pw)
            reg.save()
        fm = StudentReg()
        return HttpResponseRedirect('/vedant/student')
        # return render(request,'enroll/home.html',{'form':fm})
    else :
        fm = StudentReg()
    stud = User.objects.all()
    return render(request,'enroll/home.html',{'form':fm,'stu':stud})

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentReg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/vedant/student')
        else :
            pi = User.objects.get(pk=id)
            fm = StudentReg(instance=pi)
        return render(request,'enroll/update.html',{'form':fm})

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/vedant/student')

    
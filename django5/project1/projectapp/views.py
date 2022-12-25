from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ClientDataForm
from .models import ClientData
from .filters import ClientDataFilter

# Create your views here.

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm= AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass= fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm= AuthenticationForm()
        return render(request, 'projectapp/login.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/profile/')

def profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=ClientDataForm(request.POST)
            if fm.is_valid():
                fm.save()
                fm= ClientDataForm()
        else:
            fm= ClientDataForm()
        stud= ClientData.objects.all()
        myFilter=ClientDataFilter(request.GET,queryset=stud)        
        stud=myFilter.qs

        return render(request, "projectapp/profile.html",{'form':fm, 'stu':stud,'myFilter':myFilter})
    else:
        return HttpResponseRedirect('/login/')


 
def update_data(request, id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi = ClientData.objects.get(pk=id)
            fm = ClientDataForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Details is Updated")
        else:
            pi = ClientData.objects.get(pk=id)
            fm = ClientDataForm(instance=pi)
        return render(request,'projectapp/updatedata.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def delete_data(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi= ClientData.objects.get(pk=id)
            pi.delete()
    return HttpResponseRedirect('/profile/')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def searchbar(request):
    if request.method=='GET':
        search = request.GET.get('search',None)
        if search:
            post = ClientData.objects.filter(name__icontains=search)
            return render(request,'projectapp/search.html', {'post': post})
        else:
            post=None
            messages.info(request, "No Data")
            return HttpResponseRedirect('/project.html/')

from tkinter.messagebox import NO
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import Profil, Links
from .Forms import CreateUserForm, CreateProfileForm, ChangeUserForm, UpdateLinksForm, UpdateLinksForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import Forms
# Create your views here.


def LoginPage(request):
    Page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'User Name and Password is Incorrect')

    context = {'Page': Page}
    return render(request, 'index.html', context)


def logoutuser(request):
    logout(request)
    return redirect('LoginPage')


def RegisterUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            fullname = None
            profesion = None
            EMail = None
            Number = None
            image = None
            user1 = user
            # print(fullname,profesion,EMail,Number,image,user1)
            ins = Profil(user=request.user, Name=fullname,
                         profession=profesion, emiall=EMail, number=Number, image=image)
            ins.save()
            print(ins)
            return redirect('Home')
        else:
            messages.error(request, 'Kindly Fill form Properly')

    context = {'form': form}
    return render(request, 'index.html', context)


@login_required(login_url='LoginPage')
def home(request):
    return redirect("EditProfile")
    context = {}
    profile_obj = request.user.profil
    context['profile_obj'] = profile_obj
    if request.method == "POST":
        Instagram = request.POST.get('Instagram')
        if Instagram:
            link = Links(user=request.user, name='Instagram', link=Instagram)
            link.save()

        Facebook = request.POST.get('Facebook')
        if Facebook:
            link = Links(user=request.user, name='Facebook', link=Facebook)
            link.save()

        Twitter = request.POST.get('Twitter')
        if Twitter:
            link = Links(user=request.user, name='Twitter', link=Twitter)
            link.save()

        Youtube = request.POST.get('Youtube')
        if Youtube:
            link = Links(user=request.user, name='Youtube', link=Youtube)
            link.save()

        Other_Links = request.POST.get('Other_Links')
        if Other_Links:
            link = Links(user=request.user,
                         name='Other_Links', link=Other_Links)
            link.save()

    return render(request, 'Home.html', context)


@login_required(login_url='LoginPage')
def EditProfile(request):
    links=Links.objects.filter(user=request.user)
    form1 = CreateProfileForm(
        request.POST or None, request.FILES or None,  instance=request.user.profil)
    form2 = ChangeUserForm(request.POST or None, instance=request.user)
    form3 = UpdateLinksForm()
    if form1.is_valid() and form2.is_valid():
        form1.save()
        form2.save()
        return redirect("Profile")
    context = {'form1': form1, 'form3': form3, 'form2': form2 ,'links':links}
    return render(request, 'editprofile.html', context)



@login_required(login_url='LoginPage')
def link_form_handler(request):
    form = UpdateLinksForm(request.POST or None)
    print(request.user.id)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect("linkdetail",pk=obj.id)
    return redirect("Home")


@login_required(login_url='LoginPage')
def Profile(request):
    return render(request, 'Profile.html')


def delete_link(request, pk):
    link = Links.objects.get(pk=pk)
    link.delete()
    messages.error(request, f'{link.name} link deleted')
    return redirect('Profile')


def update_link(request, pk):
    Link=Links.objects.get(pk=pk)
    form=UpdateLinksForm(instance=Link)
    context={
        "form":form,
        "Link":Link
    }
    return render(request,"partials/link_form.html",context) 



def shareprofile(request, slu):
    profile = Profil.objects.filter(slug=slu).first()
    context = {'profile': profile}
    return render(request, 'shareprofile.html',context)
def Create_linkform(request):
    context={
        "form":UpdateLinksForm
    }
    return render(request,"partials/link_form.html",context)

def detail_link(request,pk):
    link=Links.objects.get(pk=pk)
    context={
        "Link":link
    }
    return render(request,"partials/link_detail.html",context)
def Update_linkdata(request,pk):
    Link=Links.objects.get(pk=pk)
    form=UpdateLinksForm(request.POST or None,instance=Link)
    if request.method=="POST":
        if form.is_valid():
            Link=form.save()
            return redirect("linkdetail",pk=Link.id)
        
    context={
        "form":form,
        "Link":Link,
    }
    return render(request,"partials/link_form.html",context) 

def delete_link(request,pk):
    link=Links.objects.get(pk=pk)
    link.delete()
    return HttpResponse('')

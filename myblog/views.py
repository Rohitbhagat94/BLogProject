from django.shortcuts import render,redirect
from.models import blog,contactus,profile
from myblog.forms import blog_form,contact_form
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Q 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

@never_cache
@login_required(login_url='login')
def show(request):
    data = blog.objects.all()
    return render(request,'tshow.html',{"data":data})

def base(request):
    return render(request,'base.html')

def user(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            user= User.objects.create_user(username=username,password=password)
            user.save()
            messages.success(request,"datasaved")
            return redirect("login")

        else:
            messages.info(request,"wrongpassword")
    return render(request,'user.html')

def login(request):
    if request.method == "POST":
        username= request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)

            return redirect("show")

        else:
            messages.info(request,"wrongpassword")
            return redirect("login")
    return render(request,'login.html')


@never_cache
def logout(request):
    auth.logout(request)
    return redirect("login")

# @login_required(login_url='login')
# def add(request):
#     if request.method =="GET":
#         form = blog_form()
#         return render(request,'add.html',{"form":form})

#     else:
#        form =blog_form(request.POST,request.FILES)
#        if form.is_valid():
#         form.save()
#         return redirect("show") 
#     return render(request,'add.html')


def search(request):
    s = request.POST['search']
    
    data = blog.objects.filter(title__contains=s)
    return render(request,'tshow.html',{"data":data})

@login_required(login_url='login')
@never_cache
def readmore(request,id):
    data = blog.objects.get(id=id)
    print(data)
    return render(request,'read.html',{"data":data})

def contactus1(request):
     if request.method =="GET":
        form = contact_form()
        
        data = contactus.objects.all()
            # return render(request,'contact.html',{'data':data})

        return render(request,'contact.html',{"form":form,'data':data})

     else:
       form =contact_form(request.POST,request.FILES)
       if form.is_valid():
        form.save()
        # return redirect("user") 
     return render(request,'contact.html')


def delete(request,id):
    data = blog.objects.get(id=id)
    data.delete()
    return redirect("show")

def update(request,id):
    form = blog.objects.get(id=id)

    if request.method =="GET":
        form = blog_form(instance=form)
        return render(request,'edit.html',{"form":form})

    else:
       form =blog_form(request.POST,instance=form)
       if form.is_valid():
        form.save()
        return redirect("show") 
    return render(request,'edit.html')


def profileadd(request):
    if profile.objects.filter(first_name__exact=request.user).exists():
        return redirect('pshow')
    else:
        if request.method == "POST":
            last_name = request.POST['last_name']
            email = request.POST['email']
            profile_pic = request.FILES['profile_pic']
            about_me = request.POST['aboutme']
            profile.objects.create(first_name=request.user,last_name=last_name,email=email,profile_pic=profile_pic,about_me=about_me)
            return redirect('pshow')

        return render(request,'profile.html')


def pshow(request):
    data= profile.objects.get(first_name=request.user)
    return render(request,'pro.html',{'d':data})

def Plus(request):
    if request.method == "POST":
        Title = request.POST['title']
        description = request.POST['description']
        upload_by = request.user
        
        image = request.FILES['image']
        blog.objects.create(title=Title,descrption=description,upload_by=upload_by,image=image)
        return redirect("show")
    else:
        return render(request,'add1.html')



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('tshow')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

# def change_pic(request,id):
#     aa = profile.objects.get(id=id)
#     if request.method == "POST":
#         profile_pic = request.FILES['update']
#         profile(id = id,profile_pic=profile_pic).save()
#         return redirect('pshow')
#         # return render(request,'pic.html',{"form":form})
#     else:
#         return render(request,'pic.html',{'aa':aa})

        
#    def add_profile_photo(request):
#     if request.user.is_authenticated:
#         if Profile_photo.objects.filter(user_name__exact=request.user).exists():
#             return redirect('Profile')
#         elif request.method == "POST":
#             user_name = request.user
#             profile = request.FILES['profile']

#             Profile_photo.objects.create(user_name=user_name,profile=profile)

#             return redirect('Profile')
#         else:
#             return render(request,'add_profile_photo.html')
#     else:
#         return redirect('main')

# def showprofile_photo(request):
#     if request.user.is_authenticated:
#         if Profile_photo.objects.filter(user_name__exact=request.user).exists():
#             data = Profile_photo.objects.get(user_name__exact=request.user)
#             blog = Blog.objects.filter(Your_Name__exact=request.user)
#             return render(request,'Profile.html',{'data':data,'blog':blog})
#         else:
#             return redirect('addprofile')
#     else:
#         return redirect('main')


def change_pic(request,id):
    if profile.objects.filter(first_name=request.user).exists():
            data = profile.objects.get(id = id)
            if request.method == "POST":    
                first_name = data.first_name
                last_name = data.last_name
                user = data.user
                email = data.email
                profile_pic = request.FILES['update']
                about_me = data.about_me
                profile(id=id,first_name=first_name,last_name=last_name,user=user,email=email,about_me=about_me,profile_pic=profile_pic).save()
                return redirect('pshow')
            else:
                return render(request,'pic.html')

    else :
        return redirect('pshow')
    



    


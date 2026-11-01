from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import picture


# Create your views here.

def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password) #It will compare user data with database record
        if user:
            login(request,user) 
            messages.success(request,'Login successful')
            return redirect('home')
        else:
            messages.error(request,'Username or password is incorrect')
            return redirect('login_')
    return render(request,'login_.html')
  

def register(request):
    if request.method == 'POST':
        try:
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']


            if User.objects.filter(username=username).exists():
                return render(request,'register.html',{'msg': 'Username is already taken..!'})

            user = User.objects.create_user(
                first_name=fname,
                last_name=lname,
                username=username,  
                email=email,
                password=password
            )

            
            picture.objects.create(
                user=user
            )

            return redirect('login_')

        except Exception:
            return render(request,'register.html',{'msg': 'Something went wrong. Please try again.'})

    return render(request, 'register.html')        
        
       

@login_required(login_url='login_')   
def logout_(request):
    logout(request)
    messages.success(request,'loged out successfully')
    return redirect('login_')
    

@login_required(login_url='login_')  
def profile(request):
    img = profile_img(request)
    data = picture.objects.get(user=request.user)
    return render(request,'profile.html',{'data':data,'img':img})


@login_required(login_url='login_')
def reset_password(request):
    
    if request.method == "POST":
        if "old_password" in request.POST:
            old_password = request.POST.get("old_password")
            user = request.user
 
            if user.check_password(old_password):
                return render(request, "reset_password.html", {"new": True})
            else:
                messages.error(request, "Old password is incorrect")

        elif "new_password" in request.POST:
            new_password = request.POST.get("new_password")
            user = request.user

            if user.check_password(new_password):
                messages.error(
                    request,
                    "New password cannot be the same as the old password"
                )
                return render(request, "reset_password.html", {"new": True})

            user.set_password(new_password)
            user.save()

            messages.success(request, "Password changed successfully")
            return redirect("login_")

    return render(request, "reset_password.html")




def forgot_password(request):
    global username

    if request.method == 'POST':
        if 'username' in request.POST:
            try:
                username = request.POST['username']
                if User.objects.filter(username=username).exists():
                    return render(request, 'forgot_password.html', {'new': True})
            except Exception:
                messages.error(request, 'Username is not valid')
                return render(request, 'forgot_password.html')

        elif 'password' in request.POST:
            new_password = request.POST['password']
            confirm_password = request.POST['cpassword']

            if new_password != confirm_password:
                messages.error(request, 'Passwords do not match')
                return render(request, 'forgot_password.html', {'new': True})

            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Updated the password successfully!')
            return redirect('login_')

    return render(request, 'forgot_password.html')              
    

@login_required(login_url='login_')
def update(request):
    img = profile_img(request)
    profile = picture.objects.get(user = request.user)
    user = User.objects.get(username = request.user.username)
    
    
    data = {
        'data':user,
        'image':profile
    }

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pic = request.FILES.get('image')  
        
        profile.image = pic if pic else profile.image
        profile.save() 
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        messages.success(request,'Updated Profile Successfully..!!')
        return redirect('profile')
    
    return render(request,'update.html',{"data" : data,'img':img})



def profile_img(request):
    return get_object_or_404(picture,user=request.user) 


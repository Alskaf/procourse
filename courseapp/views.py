from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Course , Lesson


def index(request):

    courses = Course.objects.order_by("-id").first()
    return render(request, 'index.html', {"courses" : courses})


def detail(request):

    lesson=Lesson.objects.all()

    return render(request, 'detail.html' , {"lesson" : lesson})

def handlelogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('rememberMe')

        try:
            # Find the user by email first, since default Auth uses username
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            
            if user is not None:
                login(request, user)
                if not remember_me:
                    # Session expires when the user closes the browser
                    request.session.set_expiry(0)
                messages.success(request, "Successfully logged in.")
                return redirect('index')
            else:
                messages.error(request, "Invalid credentials.")
                return redirect('handlelogin')
                
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials.")
            return redirect('handlelogin')

    return render(request, "auth/login.html")

def handlesignup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('handlesignup')
        
        if User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('handlesignup')
            
        try:
            user = User.objects.create_user(username=email, email=email, password=pass1)
            user.save()
            messages.success(request, "Account created successfully. Please sign in.")
            return redirect('handlelogin')
        except Exception as e:
            messages.error(request, "Error creating account. Please try again.")
            return redirect('handlesignup')

    return render(request, "auth/signup.html")

from django.shortcuts import render, redirect

#imports
from django.http import HttpResponse
from . import views
from . forms import RegistrationForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from crud.models import Employee



# Create your views here.
def createAccount(request):
    regForm = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f"Account Created Successfully")
            return redirect("signin")
        else:
            for field, erro_list in form.errors.items():
                for error in erro_list:
                    #messages.error(request, f"{field}: {error}")
                    print("f{error}")
    else:
        regForm = RegistrationForm()
        print("Correct your details and try agian")

    context = {'regForm': regForm}
    return render(request, 'auths/register.html', context)



def memberLogin(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, f"Welcome {user}")
                return redirect("dashboard")

        else:
            pass
    else:
        form = LoginForm()
       

    context = {'form': form}
    return render(request, 'auths/login.html', context)

@login_required(login_url='signin')
def userDashboard(request):
    employees = Employee.objects.all()
    
    context = {'employees':employees}
    return render(request, 'auths/dashboard.html', context)


def logUserOut(request):
    logout(request)
    messages.success(request, f"logout success")
    return redirect("index")





    

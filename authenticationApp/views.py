from django.shortcuts import render, redirect, get_object_or_404
from . forms import CreateUserForm, LoginForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User






# Authentication Models and Functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def homepage(request):
    return render(request, 'authenticationApp/index.html')
    return redirect("regitser")




def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("my-login")
        
    context = {'registerform' : form}

    return render(request, 'authenticationApp/register.html', context = context)




def my_login(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data = request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")
            
    context = {'loginform' : form}

    return render(request, 'authenticationApp/my-login.html' , context = context)

@login_required(login_url= "my-login")
def dashboard(request):
    if request.user.is_staff:  # Check if the user is an admin
        user = User.objects.all()
    else:
        user = [User.objects.get(id=request.user.id)] # Get a single user object and in a list 
        # here, get a particular login  user id and store in a list
    context = {'userinfo' : user}
    return render(request, 'authenticationApp/dashboard.html', context = context)
    
    


def user_logout(request):
    auth.logout(request)
    return redirect("")



def usersInfo(request):
    pass


def delete_info(request , id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('/dashboard')


def update_info(request , id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserUpdateForm(instance = user)
        
    return render(request, 'authenticationApp/update.html', {'updateform': form})


    



  
  

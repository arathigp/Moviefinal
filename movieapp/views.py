from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import admin, messages, auth
from movieapp.forms import MovieForm
from moviedetail.models import Movie


# Create your views here.
def home(request):
    movie = Movie.objects.all()
    return render(request,'index.html',{'movie':movie})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('movieapp:uhome')
        else:
            print("invalid credentials")
            messages.info(request, "invalid credentials")
            return redirect('movieapp:login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('movieapp:login')


def uhome(request):
    return render(request, "userhome.html")


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword= request.POST['cpassword']
        if password ==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name exist")
                return redirect('movieapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exist")
                return redirect('movieapp:register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                # print("user created")
                messages.info(request, "You are successfully registered")
                return redirect('movieapp:login')
        else:
            messages.info(request,"password is not matched")
            return redirect('register')
            return redirect('/')
    return render(request, "register.html")


def detail(request ,id):
    movie = User.objects.get(id=id)
    return render(request ,"detail.html" ,{'movie' :movie})



def update(request, id):
    movie = User.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movieapp:uhome')
    return render(request, 'update.html', {'form': form, 'movie': movie})


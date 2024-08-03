from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Certificates
from .forms import UserCreationForm,CertificatesForm
from .decoraters import authenticaterd_user
# Create your views here.

@authenticaterd_user
def home(request):
  return render(request,'index.html')

@login_required(login_url='login')
def profile(request):
  certificates = Certificates.objects.filter(user=request.user)

  return render(request,'profile.html',{'certificates':certificates})

@login_required(login_url='login')
def create(request):
  form = CertificatesForm()

  if request.method == 'POST':
    form = CertificatesForm(request.POST)
    if form.is_valid():
      certificate = form.save(commit=False)
      certificate.user = request.user  
      certificate.save()
      return redirect('home')
 
  content = {
      'form':form
   }
  return render(request,'add.html',content )




def register(request):
  form = UserCreationForm()

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
    
      return redirect('login')


  content ={
    'form':form
  }
  return render(request,'register.html',content)



def loginPage(request):

  if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request,username=username, password=password)

      if user is not None:
        login(request,user)
        return redirect('home')
      else:
        messages.info(request,'USERNAME OR PASSWORD IS INCORRECT ')

  return render(request,'login.html')


def logoutPage(request):
  logout(request)
  return redirect('login')


def delete(request,pk):
  certificates = Certificates.objects.get(id=pk)

  certificates.delete()
  
  return redirect('home')

def update(request,pk):
  certificates = Certificates.objects.get(id=pk)
  form = CertificatesForm(instance=certificates)

  if request.method == 'POST':
    form = CertificatesForm(request.POST,instance=certificates)
    if form.is_valid():
      form.save()
      return redirect('home')



  content = {'form':form}
  return render(request,'add.html',content)

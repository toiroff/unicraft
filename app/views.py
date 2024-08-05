from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from .forms import *
from .decoraters import authenticaterd_user
from .models import *

def education_form(request):
    certificate_types = CertificateType.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        certificate_type_id = request.POST.get('certificate_type')
        certificate_type = CertificateType.objects.get(id=certificate_type_id)
        
        for subject in subjects:
            score = request.POST.get(subject.name)
            if score: 
                UserSubject.objects.update_or_create(
                    user=request.user,
                    certificate_type=certificate_type,
                    subject=subject,
                    defaults={'score': score}
                )

        
     
        return redirect('profile')  
    
    context = {
        'certificate_types': certificate_types,
        'subjects': subjects,
    }
    return render(request, 'create.html', context)

def get_subjects(request, certificate_id):
    subjects = Subject.objects.filter(certificate_type_id=certificate_id)
    subjects_list = list(subjects.values('name'))
    return JsonResponse(subjects_list, safe=False)
# _______________________________________________________________________________________

@authenticaterd_user
def home(request):
  return render(request,'index.html')

@login_required(login_url='login')
def profile(request):
    certificate_types = CertificateType.objects.filter(
        usersubject__isnull=False
    ).distinct()

    certificate_subjects = {}

    for certificate_type in certificate_types:
        # Get UserSubjects for each CertificateType
        user_subjects = UserSubject.objects.filter(certificate_type=certificate_type)
        certificate_subjects[certificate_type] = user_subjects

    context = {
        'certificate_subjects': certificate_subjects
    }

    return render(request,'profile.html',context)

@login_required(login_url='login')
def create(request):
  # form = CertificatesForm()

#   if request.method == 'POST':
#     form = CertificatesForm(request.POST)
#     if form.is_valid():
#       certificate = form.save(commit=False)
#       certificate.user = request.user  
#       certificate.save()
#       return redirect('home')
 
#   content = {
#       'form':form
#    }
  return render(request,'create.html' )



def register(request):
  form = CustomUserCreationForm()

  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
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
   certificate = get_object_or_404(CertificateType, id=pk)
   user_subjects = UserSubject.objects.filter(user=request.user, certificate_type=certificate)

  
   user_subjects.delete()
    
   return redirect('profile')



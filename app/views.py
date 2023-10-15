from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

#home page access
def home(request):
    return render(request,'dummy1.html')

#doctor registration page:
def Doctor_registration(request):
    umf=DoctorUserForm()
    pmf=DoctorForm()
    d={'umf':umf,'pmf':pmf}
    if request.method=='POST' and request.FILES:
        umfd=DoctorUserForm(request.POST)
        pmfd=DoctorForm(request.POST,request.FILES)
        if umfd.is_valid() and pmfd.is_valid():
            Nud=umfd.save(commit=False)
            submittedpw=umfd.cleaned_data['password']
            Nud.set_password(submittedpw)
            Nud.save()

            Npd=pmfd.save(commit=False)
            Npd.user=Nud
            Npd.save()

            send_mail(
                'Registration',
                'Ur Hotstar Registration succefully completed.....!',
                'saisubham2501@gmail.com',
                [Nud.email],
                fail_silently=False),
            return render(request,'login.html')


    return render(request,'registration.html',d)


#Doctor login_id:
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Not active User')
    return render(request,'login.html')

#Doctor logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

# patient regetratision:
def Patient_registration(request):
    pmu=PatientUserForm()
    pmf=PatientForm()
    d={'pmu':pmu,'pmf':pmf}
    if request.method=='POST' and request.FILES:
        umfd=PatientUserForm(request.POST)
        pmfd=PatientForm(request.POST,request.FILES)
        if umfd.is_valid() and pmfd.is_valid():
            Nud=umfd.save(commit=False)
            submittedpw=umfd.cleaned_data['password']
            Nud.set_password(submittedpw)
            Nud.save()

            Npd=pmfd.save(commit=False)
            Npd.user=Nud
            Npd.save()

            send_mail(
                'Registration',
                'Ur Hotstar Registration succefully completed.....!',
                'saisubham2501@gmail.com',
                [Nud.email],
                fail_silently=False),
            return render(request,'login.html')


    return render(request,'registration1.html',d)


# patient_user_login:


#Doctor logout
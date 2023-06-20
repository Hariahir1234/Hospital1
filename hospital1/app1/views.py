from django.shortcuts import render,redirect
from .models import hospital,patient,doctor
from .forms import hospitalnew,patientnew,doctornew
from django.template import loader
from django.http import HttpResponse
from .forms import newuserform
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
 

def main(request):
    abc=loader.get_template('main.html')
    return HttpResponse(abc.render())
# Create your views here.
def registration_form(request):
    if request.method=='POST':
        abc=newuserform(request.POST)
        if abc.is_valid():
            user=abc.save()
            login(request,user)
            messages.success(request,"registration succsess full")
            return redirect('login')
        
        messages.error(request,"registration not succsess")

    abc=newuserform()
    return render(request=request,template_name="registration.html",context={'registration_detail':abc})



def index(request):
    abc=patient.objects.all()
    xyz=doctor.objects.all()
    return render (request,'main.html',{'patientdetail':abc,'doctordetail':xyz}) 

def appointment(request):
    abc=hospital.objects.all()
    return render(request,'appointment.html',{'appointmentdetails':abc})
    
    
    
def uploadpat(request):
    abc=patientnew()
    if request.method == 'POST':
        abc=patientnew(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('index')
        else:
            HttpResponse ('data is wrong')
    
    else:
        
        return render (request,'uploadpat.html',{'upload_pat':abc})        
    
def uploaddoc(request):
    abc=doctornew()
    if request.method == 'POST':
        abc=doctornew(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('index')
        else:
            HttpResponse ('data is wrong')
    
    else:
               
        return render (request,'uploaddoctor.html',{'upload_doc':abc})     

def uploadappoint(request):
    abc=hospitalnew()
    if request.method == 'POST':
        abc=hospitalnew(request.POST ,request.FILES )
        if abc.is_valid():
            abc.save()    
            return redirect('appointmentdetail')
        else:
            HttpResponse ('data is wrong')
    
    else:
        
        return render (request,'uploadappointment.html',{'upload_appoint':abc})            
    
    
def updateappointment(request,appoint_id):
    appoint_id=int(appoint_id)
    try:
        abc=hospital.objects.get(id=appoint_id)
        
    except hospital.DoesNotExist:
        return redirect ('appointmentdetail')
        
    xyz=hospitalnew(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('appointmentdetail')
         
    return render(request,'uploadappointment.html',{'upload_appoint':xyz})        
    
def updatepatient(request,pat_id):
    pat_id=int(pat_id)
    try:
        abc=patient.objects.get(id=pat_id)
        
    except patient.DoesNotExist:
        return redirect ('index')
        
    xyz=patientnew(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('index')
         
    return render(request,'uploadpat.html',{'upload_pat':xyz})    

def updatedoctor(request,doc_id):
    doc_id=int(doc_id)
    try:
        abc=doctor.objects.get(id=doc_id)
        
    except doctor.DoesNotExist:
        return redirect ('index')
        
    xyz=doctornew(request.POST or None ,instance=abc)
    if xyz.is_valid():
        
        xyz.save()
        return redirect('index')
         
    return render(request,'uploaddoctor.html',{'upload_doc':xyz})  



        
def deletepatient(request,pat_id):
    pat_id=int(pat_id)
    try:
        abc=patient.objects.get(id=pat_id)
    except patient.DoesNotExist:
        return redirect('index')
    abc.delete()
    return redirect ('index')
        
            
def deletedoctor(request,doc_id):
    doc_id=int(doc_id)
    try:
        abc=doctor.objects.get(id=doc_id)
    except doctor.DoesNotExist:
        return redirect('index')
    abc.delete()
    return redirect ('index')
                    
def deleteappointment(request,appoint_id):
    appoint_id=int(appoint_id)
    try:
        abc=hospital.objects.get(id=appoint_id)
    except hospital.DoesNotExist:
        return redirect('appointmentdetail')
    abc.delete()
    return redirect ('appointmentdetail')
                           

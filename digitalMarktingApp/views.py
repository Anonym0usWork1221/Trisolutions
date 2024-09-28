from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from digitalMarktingApp.models import ContactUS


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        second_name = request.POST.get('surname')
        email = request.POST.get('email')
        desc = request.POST.get('message')
        
        redirect_from = request.POST.get('next')
         
        if name != "" and email != "" and desc != "": 
            contact = ContactUS(first_name=name, sur_name=second_name, email=email, desc=desc, date=datetime.today())
            contact.save()
            # messages.success(request, 'Your message has been sent!')
            return HttpResponseRedirect(redirect_from)
                    
        else:
            # messages.error(request, 'Please fill all the required fields.')
            return HttpResponseRedirect(redirect_from)
        
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')


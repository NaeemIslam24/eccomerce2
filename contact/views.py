from django.shortcuts import render
from . models import *
# Create your views here.

def contact(request):
    template = 'contact-us.html'
    contact = Contact.objects.all()
    
    if request.method == 'POST':

        name = request.POST.get('name')
        mail = request.POST.get('email')
        sub = request.POST.get('subject')
        sms = request.POST.get('message')
        print('-----------------------------------')
        print(name, mail, sub, sms)
        data = Contact(name=name, email=mail, subject=sub, sms=sms)
        data.save()
        
  


    return render(request, template_name=template)

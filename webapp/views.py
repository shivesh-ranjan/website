from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .models import Contact, MailList

# Create your views here.
def home(request):
    if request.method=="POST":
        email = request.POST["newsEmail"]
        if len(email)<5:
            messages.error(request, "Please enter a valid Mail ID!")
        elif MailList.objects.filter(Email=email).first():
            messages.warning(request, "You are already on the List!")
        else:
            maillist=MailList(Email=email)
            maillist.save()
            messages.success(request, "Mail Added!")
    return render(request ,'webapp/home.html')

def contact(request):
    if request.method=="POST":
        name = request.POST["contactName"]
        email = request.POST["contactEmail"]
        phone = request.POST["contactPhone"]
        issue = request.POST["contactIssue"]
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(issue)<4:
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(Name=name, Email=email, Phone=phone, Issue=issue)
            contact.save()
            messages.success(request, "Form submitted!")
    return render(request, 'webapp/contact.html')
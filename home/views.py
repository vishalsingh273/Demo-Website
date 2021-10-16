from django.shortcuts import render,HttpResponse
from home.models import Contact

def home(request):
  return render(request,'home.html')

def about(request):
   # return HttpResponse("this is about the website")
   return render(request, 'about.html')

def project(request):
   # return HttpResponse("this is about the project")
   return render(request, 'project.html')

def contact(request):
   if request.method=="POST":
      name = request.POST['name']
      email= request.POST['email']
      phone= request.POST['phone']
      Issue= request.POST['Issue']
      print(name,email,phone,Issue)
      contact=Contact(name=name,email=email,phone=phone,Issue=Issue)
      contact.save()

   return render(request, 'contact.html')



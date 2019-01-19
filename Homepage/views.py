from django.shortcuts import render
from django.http import HttpResponse 
from django.http import HttpRequest
# Create your views here.
def show (request):
    response= HttpResponse()
    response.write('hello world')
    return response
#  function processing request and reponse  in web app
def showtest(request):
   
    response = HttpResponse()
    response.write('long is here')
    return response

def showPage(request):
    #  CALL PAGE HTML iN templates
    return render(request,'pageHome.html')
def showContact(request):
    return render(request,'contact.html')
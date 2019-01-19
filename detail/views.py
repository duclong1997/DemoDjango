from django.shortcuts import render
from django.http import HttpResponse 
from django.http import HttpRequest
from .models import post
# Create your views here.
def showDetail(request):
    reponse = HttpResponse()
    reponse.write('hello detail!')
    return reponse

def showList(request):
    #  get list data in parameter posts send html 
    #  order by column datetime asc
    data = {'posts':post.objects.all().order_by('datetime')}
    #  go view showList.html and parameter: data
    return render(request,'showLIst.html',data)

    # id: parameter -> view
def showPost(request, id):
    spost ={'post':post.objects.get(id=id)}
    return render(request,'showpost.html',spost)

    
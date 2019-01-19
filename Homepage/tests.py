from django.test import TestCase
#   reponse view 
from django.http import HttpResponse
# Create your tests here.
#  create function test 
def  show(request):
    reponse= HttpResponse()
    reponse.write('hello world!')
    reponse.writelines('Test')
    return reponse  

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def debo(request):
    my_dict={'insert':''}
    return render(request,'debo.html',context=my_dict)

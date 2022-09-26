from django.shortcuts import render
from django.http import HttpResponse


#When you call this home page the browser wil send you a request witth,
#a whole lot of data coming from the website that you can use
def home_page(request):

    return HttpResponse('Hello world')


from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


#When you call this home page the browser wil send you a request witth,
#a whole lot of data coming from the website that you can use
def home_page(request):

    #this will return a queryset of all your leads as a list
    #meaning if you want to display all of the data one by one you need to run
    #a for loop on the html page {%for lead in leads%}
    leads = Lead.objects.all()
    context = {
        "leads": leads,
    }

    #context takes a dictionary that can be passed down to our webpage
    #you can access the context data by wrting {{name}} it will give you the 
    #output of the dictionary on your html file
    # context = {
    #     "name":"joe",
    #     "age":27
    # }

    #this will work if you want to find the templates in your app directory
    # return render(request,'leads/home_page.html')

    #this will work if you want to get the templates after you sett the template settings to 
    #BASE_DIR / 'templates'
    return render(request,'index.html',context)


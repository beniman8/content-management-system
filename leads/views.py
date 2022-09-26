from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


#When you call this home page the browser wil send you a request witth,
#a whole lot of data coming from the website that you can use
def lead_list(request):

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
    return render(request,'leads/lead_list.html',context)


def lead_detail(request, pk):
    #if you want to return a certain value to our function
    #add it to the function in our case pk. 
    #now when you type the url of the detail view with the lead/1
    #the value 1 gets sent back to us if you set up the url to
    #receive the pk in its route     path('<pk>/', lead_detail),

    # print(pk)

    lead = Lead.objects.get(id=pk)

    context = {
        'lead':lead,
    }
    return render(request,'leads/lead_detail.html',context)


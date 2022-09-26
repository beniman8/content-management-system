from django.shortcuts import render
from django.http import HttpResponse


#When you call this home page the browser wil send you a request witth,
#a whole lot of data coming from the website that you can use
def home_page(request):

    #this will work if you want to find the templates in your app directory
    # return render(request,'leads/home_page.html')

    #this will work if you want to get the templates after you sett the template settings to 
    #BASE_DIR / 'templates'
    return render(request,'index.html')


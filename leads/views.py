from multiprocessing import context
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm,LeadModelForm
from django.views.generic import TemplateView,ListView,DeleteView,UpdateView,DetailView,CreateView


#CRUD+L  CREATE RETRIEVE/READ UPDATE DELETE + LIST

######################### LANDINGPAGE VIEW ##########################################

class LandingPageView(TemplateView):
    template_name = 'landing.html'

def landing_page(request):
    return render(request,'landing.html')


################################################# VIEW THE LEADS  ########################################################




#The class Base view version 

class LeadListView(ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()

    #object_list is the key set by this class we will change it to leads
    context_object_name = 'leads'


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





#The class Base view version 

class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

    #This will automatically grab the pk for us

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





################################################### CREATE THE LEADS  ###########################################

#The class Base view version 
class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')
  

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        print('Receiving a post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            #with a model form all you have to write is form.save() to save all the data in your form
            form.save()
            return redirect('/leads')
    context = {
        # "form": LeadForm(),
        "form": form,
    }
    return render(request,'leads/lead_create.html',context)


## When you only use a regular form###

# def lead_create(request):

#     # print(request.POST)
#     #Result of when the form button get pressed and we receive the post data coming from the front end or html page
#     #<QueryDict: {'csrfmiddlewaretoken': ['KxbZvNP0TeM9l1S2aFx94cZ2xsv24KSPL9x48fVsXqIA0drJqr0vkzUGu4ux7IjD'], 'first_name': ['beni'], 'last_name': ['kangu'], 'age': ['34']}>
#     form = LeadForm()
#     if request.method == "POST":
#         print('Receiving a post request')
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print('form is valid')
#             # print(form.cleaned_data)
#             #The clean data just returns a formated dictionary that we can use
#             # {'first_name': 'jhon', 'last_name': 'doeetry', 'age': 45}

#             #we are retreaving the data from the dictionary so that we can use it to create the lead in the database
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             #for now just grab the first agent
#             agent = Agent.objects.first()

#             #we create a new lead and pass it all the data that's needed coming from the form
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent,
#             )

#             #after the lead has been created return us to the main page with all our leads
#             return redirect('/leads')
    
#     #when we call LeadForm() we are sending and creating a form that can be accesed to the front end
#     #This will return a html form with the values that are available in the form you have created.
#     context = {
#         # "form": LeadForm(),
#         "form": form,
#     }
#     return render(request,'leads/lead_create.html',context)



################################################### UPDATE THE LEADS  ###########################################

#The class Base view version 
class LeadUpdateView(UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')


def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    #we grab an instance of our lead form with this id and with show it in our html front page
    #so that we can edit our instance that is saved in our database and save it again
    #with the new edited content
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
        
    context = {
        'form':form,
        "lead": lead,
    }
    return render(request, 'leads/lead_update.html',context)

# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         print('Receiving a post request')
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print('form is valid')
#             # print(form.cleaned_data)
#             #The clean data just returns a formated dictionary that we can use
#             # {'first_name': 'jhon', 'last_name': 'doeetry', 'age': 45}

#             #we are retreaving the data from the dictionary so that we can use it to update the lead in the database
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']

#             #we update this new lead
#             lead.first_name=first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()


#             #after the lead has been updared return us to the main page with all our leads
#             return redirect('/leads')
    
#     context = {
#         'form':form,
#         "lead": lead,
#     }
#     return render(request, 'leads/lead_update.html',context)


################################################### DELETE THE LEADS  ###########################################

#The class Base view version 
class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')


def lead_delete(request,pk):
    
    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('/leads')
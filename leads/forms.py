from django import forms

#here is where we create forms by using the built django class Form
#this will help us create leads by using a form in the front end rather
#than only being able to create leads from the backend.

class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
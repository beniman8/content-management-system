from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead

from django.contrib.auth import get_user_model

User = get_user_model()
#here is where we create forms by using the built django class Form
#this will help us create leads by using a form in the front end rather
#than only being able to create leads from the backend.


#This is a way to turn your model in the database in to a form
class LeadModelForm(forms.ModelForm):
    
    #The meta tells django to grab a certain model and create a form using the data from the fields
    class Meta:
        model = Lead
        fields = (
                'first_name',
                'last_name',
                'age',
                'agent',
        )

#this is how to creat a form
class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}




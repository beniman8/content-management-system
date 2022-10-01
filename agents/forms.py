from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from leads.models import Agent

from django.contrib.auth import get_user_model


class AgentModelForm(forms.ModelForm):
    
    #The meta tells django to grab a certain model and create a form using the data from the fields
    class Meta:
        model = Agent
        fields = (
                'user',
        )






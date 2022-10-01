from django.db import models
from django.db.models.signals import post_save
#If you dont want to create your own user model you can grab the one created by django
# from django.contrib.auth import get_user_model
# User = get_user_model

#we will be creating our user model


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ''' Make sure to go to your setting and create a AUTH_USER_MODEL = "app_name.User" 
        This will help django find this costume user model instead of the one that 
        comes premade with django.
    
    change the app_name to your app name !!!!! mine is leads yout might be different
    '''
    pass

class UserProfile(models.Model):
    user = user = models.OneToOneField("User", on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.user.username

class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    #By using the agent as a foreign key , you are saying one agent can have many leads
    #but also one lead can not hvae many agents or only one agent
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'Lead Name: {self.first_name}  |  Agent Name: {self.agent.user.username}'

class Agent(models.Model):
    #we are creating one agent for everyone user so we need a one to one relationship and not a foreingkey
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    

def post_user_create_signal(sender,instance,created,**kwargs):
    ''' This here is going to be used to create a user profile of the person once the user is created.

        instance is a copy of the sender so in our case it will be the user

        created is a true are false value if your user has been created and saved
    
    '''

    if created:
        UserProfile.objects.create(user=instance)
    


#This here is saying check the user class if the save method is activated
#run the post_user_create_signal function
post_save.connect(post_user_create_signal,sender=User)

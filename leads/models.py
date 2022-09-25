from django.db import models

class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    #By using the agent as a foreign key , you are saying one agent can have many leads
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

class Agent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
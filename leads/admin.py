from django.contrib import admin
from .models import Lead,Agent,User,UserProfile

#You register the models you created so that you can see it in your admin panel
#It makes it easier for you to add delete or edit them on the backe end 
#Rather than to do it on the terminal ---- not so fun
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(User)
admin.site.register(UserProfile)

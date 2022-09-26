from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update,lead_delete


app_name='leads'
urlpatterns = [
    path('', lead_list),    
    path('<int:pk>/', lead_detail),
    path('<int:pk>/update/', lead_update),
    path('<int:pk>/delete/', lead_delete),
    path('create/', lead_create),


]


#if you have only <pk> as your primary key python will try to match the url as if it was a pk
#so to combat that we either have to put evry other url beffore the pk path
#or simply add the type infront of it so django know if it is not of that type go to 
#the next path <int:pk>
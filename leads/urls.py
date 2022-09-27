from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update,lead_delete


app_name='leads'
urlpatterns = [
    path('', lead_list, name='lead-list'),    
    path('<int:pk>/', lead_detail, name='lead-detail'),
    path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    path('create/', lead_create, name='lead-create'),


]


#if you have only <pk> as your primary key python will try to match the url as if it was a pk
#so to combat that we either have to put evry other url beffore the pk path
#or simply add the type infront of it so django know if it is not of that type go to 
#the next path <int:pk>
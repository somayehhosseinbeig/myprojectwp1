from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name= 'index'),
    path("somayeh",views.somayeh,name ="somayeh"),
    path("arnika",views.arnika, name="arnika"),
    path("<str:name>",views.greet,name="greet")
]
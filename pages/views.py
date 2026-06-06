
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
# Class-based views
# Pascal Notation - SweetHomeAlabama
class HomePageView(TemplateView): # OOP - Object Oriented Programming (Inheritance)
    template_name = "home.html" # Attribute
    
    def get_context_data(self, **kwargs): # Method
        context = super().get_context_data(**kwargs) 
        context["name"] = "Ariana"
        context["address"] = "123 Main St, Anytown, Mexico"
        context["email"] = "ariana@gmail.com"
        return context
    

class AboutPageView(TemplateView):
    template_name = "about.html"

# Function-based views
def contact_me(request):
    # return HttpResponse("Hello World from a Function Based View")
    contact_info = {
        "name": "Ariana",
        "address": "123 Main St, Anytown, Mexico",
        "email": "ariana@gmail.com"
    }
    
    
    
    return render(request, "contact.html", contact_info)

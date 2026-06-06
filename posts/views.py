from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView): #GET request -> List
    #template_name attribute renders a specific html file
    template_name = "list.html"
    #model attribute let django know which model (table) we want to retrieve the data
    model = Post
    # context_object_name attribute allow us to change the name on how we call it inside of the template
    context_object_name = "posts"

class PostDetailView(DetailView): #GET request ->Single Object
    template_name = "detail.html"
    model = Post
    context_object_name = "single_post"


class PostCreateView(CreateView): #POST request -> New object / empty form (html)
    template_name = "new.html"
    model = Post
    fields = ["title", "subtitle", "body"] #fields attribute let


    def form_valid(self, form):
        form.instance.author = User.objects.last() 
        print(form)
        print(form.instance)
        print(form.instance.author)
        return super().form_valid(form)

class PostUpdateView(UpdateView): #POST request -> alter an existing object / filled form
    template_name = "edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]


class PostDeleteView(DeleteView): #POST request -> form to delete the object
    template_name = "delete.html"
    model = Post
    #success_url attribute allow us to redirect the users to another view if request successful
    success_url = reverse_lazy("post_list")
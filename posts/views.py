from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from posts.models import Status,Post
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    template_name= "posts/new.html"
    model= Post
    fields =[
        "title","subtitle","author",
        "body", "status"
    ]

class PostDetailView(DetailView):
    templete_name = "posts/detail.html"
    model = Post

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model= Post
    fields =[
        "title", "subtitle" ,"body",
        "status"
    ]

class PostDeleteView(DeleteView):
    template_name ="posts/delete.html"
    model=Post
    success_url = reverse_lazy("list")

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post



# Create your views here.

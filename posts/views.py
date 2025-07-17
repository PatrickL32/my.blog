from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from posts.models import Status,Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
)

class PostCreateView(LoginRequiredMixin,CreateView):
    template_name= "posts/new.html"
    model= Post
    fields =[
        "title","subtitle",
        "body", "status"
    ]

def form_valid(self,form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostDetailView(DetailView):
    templete_name = "posts/detail.html"
    model = Post


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = "posts/edit.html"
    model= Post
    fields =[
        "title", "subtitle" ,"body",
        "status"
    ]

def test_func(self):
    post = self.get_object()
    return post.author==self.request.user

class PostDeleteView(DeleteView):
    template_name ="posts/list.html"
    model=Post
    success_url = reverse_lazy("list")

class PostListView(ListView):
    template_name = "posts/list.html"
    model=Post

class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model=Post 
    
def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    draft = Status.objects.get(name="draft")
    context["title"]="Draft"
    context["post_list"] = (
        Post.objects.all()
        .filter(status= draft)
        .filter(author=self.request.user)
        .order_by("created_on").reverse()
    )
    return context

class ArchievedPostListView( LoginRequiredMixin,ListView):
    template_name = "posts/list.html"
    model = Post

def get_caught_data(self,**kwargs):
    context= super().get_caught_data(**kwargs)
    archived = Status.objects.get(name="archived")
    context["title"] = "Archived"
    context["post_list"] = (
        Post.objects.all()
        .filter(status=archived)
        .order_by("created_on").reverse()
    )
    return context
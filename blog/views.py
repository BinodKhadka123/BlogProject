from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import SignUpForm,PostForm
from .models import *
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form}) 
class PostListView(ListView):
    model = Post
    template_name = 'blog/bloglist.html'  
    context_object_name = 'posts'     
    ordering = ['-created_at']
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blogdetail.html' 
    context_object_name = 'post'
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-list')  
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_post.html'  

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')  
    template_name = 'blog/delete_post.html'  

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
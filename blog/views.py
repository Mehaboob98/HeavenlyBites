# blog/views.py
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Your template for listing posts
    context_object_name = 'posts'
    ordering = ['-publication_date']  # Order posts by publication date (newest first)
    paginate_by = 10  # Number of posts per page

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # Your template for displaying a single post
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'  # Your template for creating a new post
    fields = ['title', 'content']  # Fields to include in the form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
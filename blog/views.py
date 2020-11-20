from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post


# def home(request):
#     context = { 'posts': Post.objects.all() }
#     return render(request, 'blog/home.html', context, )

class PostListView(ListView):
    """ Displays all posts in the db. This has been tweaked. This is equivalent to the function based code """
    model = Post
    template_name = 'blog/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    """ This view displays a single post based on its id(pk) """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """ This view allows users to create a new post """
    model = Post
    fields = ['title', 'content']

    # This overrides form valid method. To set current logged in user as author
    def form_valid(self, form):
        # Set form author to logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ This view allows users to create a new post """
    model = Post
    fields = ['title', 'content']

    # This overrides form valid method. To set current logged in user as author
    def form_valid(self, form):
        # Set form author to logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Validate owner of post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # Redirects to homepage

    # Validate user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

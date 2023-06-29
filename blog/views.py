from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Post, Announcement
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView)



class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class LatestPostListView(ListView):
    model = Post
    template_name = 'blog/latest_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.all().order_by('-date_posted')[:5]
        if posts:
            return posts
        messages.warning(self.request, 'No Posts Yet')


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        if (form.instance.author == self.request.user) or (self.request.user.is_staff):
            return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if (self.request.user == post.author) or (self.request.user.is_staff):
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if (self.request.user == post.author) or \
        (self.request.user.is_staff):
            return True
        return False
    

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'blog/announcements.html'
    context_object_name = 'announcements'
    paginate_by = 5

    def get_queryset(self):
        return Announcement.objects.all().order_by('-date_posted')
    

class UserAnnouncementListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Announcement
    template_name = 'blog/user_announcements.html'
    context_object_name = 'announcements'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Announcement.objects.filter(author=user).order_by('-date_posted')
    
    def test_func(self):
        return self.request.user.is_staff


class AnnouncementDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Announcement
    
    def test_func(self):
        return self.request.user.is_staff


class AnnouncementCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Announcement
    fields = ['title', 'content']
        

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_staff


class AnnouncementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content']

    def form_valid(self, form):
        if ((form.instance.author == self.request.user) and (self.request.user.is_staff)) or \
        ((form.instance.author != self.request.user) and (self.request.user.is_staff)):
            return super().form_valid(form)
    
    def test_func(self):
        announcement = self.get_object()
        if (self.request.user == announcement.author) or (self.request.user.is_staff):
            return True
        return False
    

class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announcement
    success_url = '/announcements/'

    def test_func(self):
        self.get_object()
        if self.request.user.is_staff:
            return True
        return False


class BlogSearchView(ListView):
    model = Post
    success_url = 'search/'
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
            query =  self.request.GET.get('q')
            queryset = Post.objects.filter(title__icontains=query).order_by('-date_posted')
            if query == '':
                messages.warning(self.request, 'Please enter a search')
            elif query and not queryset:
                messages.warning(self.request, 'No matches were found')
            else:
                messages.success(self.request, f'{queryset.count()} matches were found')
                return queryset

            
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
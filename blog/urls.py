from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView, 
                    PostUpdateView, PostDeleteView, UserPostListView,
                    LatestPostListView, AnnouncementListView, AnnouncementDetailView,
                    AnnouncementUpdateView, AnnouncementDeleteView, UserAnnouncementListView,
                    AnnouncementCreateView, BlogSearchView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/latest/', LatestPostListView.as_view(), name='latest-posts'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/', BlogSearchView.as_view(), name='blog-search'),
    path('announcements/', AnnouncementListView.as_view(), name='announcements'),
    path('user/announcements/<str:username>/', UserAnnouncementListView.as_view(), name='user-announcements'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('announcements/new/', AnnouncementCreateView.as_view(), name='announcement-create'),
    path('announcements/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement-update'),
    path('announcements/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement-delete'),
    path('about/', views.about, name='blog-about'),
]
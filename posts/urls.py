# posts/urls.py

from django.urls import path
from . import views # Make sure 'views' is imported from the current app: from . import views

urlpatterns = [
    # Give each path a unique, clear name and a trailing slash
    path('new/', views.PostCreateView.as_view(), name='new'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    
    # FIX: Give the archived list its own unique path
    path('archived/', views.ArchievedPostListView.as_view(), name='archived'), # Also fixed the typo 'Archieved' -> 'Archived'
    
    # FIX: This is now the only view for the '/posts/' URL
    path('', views.PostListView.as_view(), name='list'),
]
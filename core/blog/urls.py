from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from . import views

app_name = 'blog'

urlpatterns = [
    # path('fbv-index', views.indexView, name='fbv-index'),      
    # path('cbv-index', TemplateView.as_view(template_name='index.html')),   
    # path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    # path('go-to-index', RedirectView.as_view(pattern_name='blog:cbv-index'), name='go-to-index'),
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'), 
    path('api/v1/', include('blog.api.v1.urls')),
]
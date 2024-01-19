from django.urls import path
from django.views.generic import TemplateView, RedirectView
from . import views

app_name = 'blog'

urlpatterns = [
    path('fbv-index', views.indexView, name='fbv-index'),      
    # path('cbv-index', TemplateView.as_view(template_name='index.html')),   
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('go-to-index', RedirectView.as_view(pattern_name='blog:cbv-index'), name='go-to-index'),
]
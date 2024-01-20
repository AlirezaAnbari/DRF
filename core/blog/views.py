from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView
from .models import Post
from .forms import PostForm

# Create your views here.
def indexView(request):
    '''
    a function based view to show index page
    '''
    return render(request, "index.html")

class IndexView(TemplateView):
    '''
    a class based view to show index page
    '''
    
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context
    
class PostListView(ListView):
    # model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    # paginate_by = 2
    ordering = '-id'
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
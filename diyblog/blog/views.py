from django.shortcuts import render

from .models import Blog, Comment, Blogger

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of blogs 
    num_blogs = Blog.objects.all().count()

    # Generate count of bloggers
    num_bloggers = Blogger.objects.all().count()

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
    }

    # Render the HTML template index.html with the data in the context var
    return render(request, 'index.html', context=context)

from django.views import generic

class BlogListView(generic.ListView):
    model = Blog
    
    paginate_by = 5


class BloggerListView(generic.ListView):
    model = Blogger


class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerDetailView(generic.DetailView):
    model = Blogger

from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment

    fields = ['description']

    def get_context_data(self, **kwargs):
        # Call the base implementation to get a context
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # Get the blog object from the "pk" URL parameter and add it to the context
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])

        return context
    
    def form_valid(self, form):
        """Add author and associated blog to form data before setting it as valid so saved to model"""
        # Add logged in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Call super class form validation behaviour
        return super(CommentCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.kwargs['pk']})
    
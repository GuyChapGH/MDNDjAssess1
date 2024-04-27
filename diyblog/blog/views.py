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
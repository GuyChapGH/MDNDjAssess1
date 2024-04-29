from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    """Model representing a blog post"""
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Add blog here")
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('Blogger', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Return the URL to access a particular instance of the model"""
        return reverse('blog-detail', args=[str(self.id)])
    
class Comment(models.Model):
    """Model representing a comment on a blog"""
    description = models.TextField(help_text="Enter comment about blog here")
    date_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # Blog can have multiple comments. Comment is for one blog.

    class Meta:
        ordering = ['date_time']

    def __str__(self):
        return self.description[:75]
        # Comment names in admin site are created by truncating the comment description to 75 characters

class Blogger(models.Model):
    """Model representing a blogger"""
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(help_text="Enter short biography here")

    def __str__(self):
        # Not sure about this: could be self.author.username ??
        return str(self.author)
    
    def get_absolute_url(self):
        """Return the URL to access a particular instance of the model"""
        return reverse('blogger-detail', args=[str(self.id)])
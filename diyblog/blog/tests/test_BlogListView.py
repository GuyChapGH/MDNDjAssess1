from django.test import TestCase

from django.urls import reverse, reverse_lazy

from django.contrib.auth import get_user_model
User = get_user_model()

from blog.models import Blog, Blogger, Comment

# Create your tests here.

class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        # Create test_user object
        test_user = User.objects.create_user(username='test_user', password='1X<ISRUkw+tuK')
        test_user.save()
        # Create blogger object
        blogger = Blogger.objects.create(author=test_user, bio='test bio')
        
        
        # Create 8 blogs for pagination tests
        number_of_blogs = 8

        for blog_id in range(number_of_blogs):
            Blog.objects.create(title=f'Test Case {blog_id}', description='Blog test case', author=blogger)
        

    def test_view_url_exists_at_desired_locatino(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')
    
    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blog_list']), 5)


from django.test import TestCase

from django.contrib.auth import get_user_model
User = get_user_model()

from blog.models import Blog, Blogger, Comment

# Create your tests here.

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        # Create test_user object
        test_user = User.objects.create_user(username='test_user', password='1X<ISRUkw+tuK')
        test_user.save()
        # Create blogger object
        blogger = Blogger.objects.create(author=test_user, bio='test bio')
        # Create blog object
        Blog.objects.create(title='Test Case 1', description='First test case', author=blogger)

    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_date_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')
    
    def test_author_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_title(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = blog.title
        self.assertEqual(str(blog), expected_object_name)

    def test_blog_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        # This will also fail if URLConf is not defined
        self.assertEqual(blog.get_absolute_url(), '/blog/blog/1')
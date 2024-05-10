from django.test import TestCase

from django.contrib.auth import get_user_model
User = get_user_model()

from blog.models import Blog, Blogger, Comment

# Create your tests here.

class BloggerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        # Create test_user object
        test_user = User.objects.create_user(username='test_user', password='1X<ISRUkw+tuK')
        test_user.save()
        # Create blogger object
        Blogger.objects.create(author=test_user, bio='test bio')
        

    def test_author_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_bio_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_object_name_is_author(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = str(blogger.author)
        self.assertEqual(str(blogger), expected_object_name)

    def test_blog_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        # This will also fail if URLConf is not defined
        self.assertEqual(blogger.get_absolute_url(), '/blog/blogger/1')
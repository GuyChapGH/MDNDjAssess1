from django.test import TestCase

from django.contrib.auth import get_user_model
User = get_user_model()

from blog.models import Blog, Blogger, Comment

# Create your tests here.

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        # Create test_user object
        test_user = User.objects.create_user(username='test_user', password='1X<ISRUkw+tuK')
        test_user.save()
        # Create blogger object
        blogger = Blogger.objects.create(author=test_user, bio='test bio')
        # Create blog object
        blog = Blog.objects.create(title='Test Case 1', description='First test case', author=blogger)
        # Create comment object
        Comment.objects.create(description='Test Comment 1', author=test_user, blog=blog)



    def test_description_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_date_time_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('date_time').verbose_name
        self.assertEqual(field_label, 'date time')

    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')
    
    def test_blog_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('blog').verbose_name
        self.assertEqual(field_label, 'blog')

    def test_object_name_is_truncated_description(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = comment.description[:75]
        self.assertEqual(str(comment), expected_object_name)

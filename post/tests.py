from django.test import TestCase
from .models import Post,Stream,Tag,Likes

# Create your tests here.
class TestPost(TestCase):
    def setUp(self):
        self.new_post=Post(image = "default.jpg", title="Title", caption='hello world', user='user')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_image(self):
        new_p=self.new_post
        new_p.save_image()
        posts=Post.get_posts()
        self.assertTrue(len(posts)>0)

    def update_image(self):
        new_p=self.new_post
        new_p.update_caption()
        posts=Post.get_posts()
        self.assertTrue(len(posts)==0)

    def test_delete_image(self):
        new_p=self.new_post
        new_p.delete_image()
        posts=Post.get_posts()
        self.assertTrue(len(posts)==0)

        
class TestLike(TestCase):
    def setUp(self):
        self.new_user=user(first_name='John', last_name='Doe', username='user', email='user@gmail.com',password='user')
        self.new_user.save()
        user=Likes(author=1, post=1)
        user.save()

    def test_instance(self):
        self.assertTrue(isinstance(Likes))
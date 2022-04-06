from django.test import TestCase
from .models import Post,Stream,Tag

# Create your tests here.
class PostTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Tag(name="Study")
        # self.cat.save_tag()
        
        self.caption = Post(caption='image test', tag=self.cat)
        self.caption.save_caption()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.user, Post))

    def tearDown(self):
        self.caption.delete_caption()
        self.cat.delete_tag()
        self.loc.delete_user()

    def test_save_method(self):
        self.image.save_image()
        caption  = Post.objects.all()
        self.assertTrue(len(caption)>0)
        
    def test_search_by_user(self):
        user = Post.search_by_category('fashion')
        self.assertTrue(len(user)>0)
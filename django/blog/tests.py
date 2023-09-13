from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')

        cls.test_user = User.objects.create_user(username='test_user', password='test_password')

        test_post = Post.objects.create(category=test_category, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')

    def test_postobjects_manager(self):
        #test_user = User.objects.create_user(username='test_user', password='test_password')
        published_post = Post.objects.create(category_id=1, title='Published Post', status='published', author=self.test_user)
        draft_post = Post.objects.create(category_id=1, title='Draft Post', status='draft', author=self.test_user)

        published_posts = Post.postobjects.get_queryset()

        self.assertIn(published_post, published_posts)

        self.assertNotIn(draft_post, published_posts)
    
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user')
        self.assertEqual(excerpt, 'Post Excerpt')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(cat), "django")
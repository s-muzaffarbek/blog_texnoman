from django.db import models
from django.utils.text import slugify
from account.models import MyUser


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Blog(models.Model):
   title = models.CharField(max_length=255)
   slug = models.SlugField(max_length=255, unique=True)
   content = models.TextField(blank=True, null=True)
   created = models.DateTimeField(auto_now_add=True)
   image = models.ImageField(upload_to='blog/')
   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_blog')
   user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)
   tags = models.ManyToManyField(Tag, related_name='tag_blog')
   views = models.IntegerField(default=0)

   def __str__(self):
       return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment_blog')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comment_user')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content




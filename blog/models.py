from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"         
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True)
    author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    #New fields
    sub_title = models.CharField(max_length=255,blank=True,null=True)
    img = models.ImageField(upload_to='blog/images/',blank=True,null=True)
    category = models.ForeignKey(Category,related_name='blog_categories',on_delete=models.CASCADE,blank=True,null=True)
    
    class Meta:
       ordering = ['-created_at',]
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title} - {self.author.username}"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='blog_comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog.title}"
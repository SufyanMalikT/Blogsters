from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CommentForm
from django.db.models import Count
# Create your views here.


def blog_home(request):
    blogs = Blog.objects.all()
    authors = User.objects.filter(is_staff=True)
    blogs= blogs[0:3]
    return render(request,'blog/home.html',{'blogs':blogs, 'authors':authors})

# @login_required
def blog_details(request, slug):
    blog = get_object_or_404(Blog,slug=slug)

    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.blog = blog
            new_comment.author = request.user
            new_comment.save()
            return redirect('blog_details', slug=blog.slug)
        
    else:
        comment = CommentForm()

    comments =  blog.comments.all()
    return render(request,'blog/blog_details.html',{'blog':blog, 'commentform':comment, 'comments':comments})


def blog_about(request):
    return render(request,'blog/about.html',{})


def blog_cat(request):

    # Fetch all categories and blogs
    categories = Category.objects.annotate(count_blogs=Count('blog_categories')).order_by('-count_blogs')[:5]
    # blogs = Blog.objects.all()

    blogs_by_categories = []

    for cat in categories:
        blogs_by_cat = Blog.objects.filter(category=cat)

        blogs_by_cat_chunks = [blogs_by_cat[i:i+3] for i in range(0,len(blogs_by_cat),3)]
        blogs_by_categories.append({'category':cat,'blogs':blogs_by_cat, 'blogs_chunk':blogs_by_cat_chunks})


    # Group blogs by categories
    # Create a list to hold the blogs grouped by category
    
    # for category in categories:
    #     list = []
    #     for blog in blogs:
    #         if blog.category == category:
    #             list.append(blog)
                
    #     list2 = [list[i:i+3] for i in range(0,len(list),3)]
    #     blogs_by_categories.append({'category':category,'blogs':list ,'blogs_chunk':list2})
    return render(request,'blog/blogs_cat.html',{'blogs_by_categories':blogs_by_categories})
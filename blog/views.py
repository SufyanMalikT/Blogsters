from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Blog, Comment, Category, ProfilePic, Profile, Messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CommentForm, ProfilePicForm
from django.db.models import Count
from django.contrib import messages
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


    blogs_by_categories = []

    for cat in categories:
        blogs_by_cat = Blog.objects.filter(category=cat)

        blogs_by_cat_chunks = [blogs_by_cat[i:i+3] for i in range(0,len(blogs_by_cat),3)]
        blogs_by_categories.append({'category':cat,'blogs':blogs_by_cat, 'blogs_chunk':blogs_by_cat_chunks})


    
    
    return render(request,'blog/blogs_cat.html',{'blogs_by_categories':blogs_by_categories})


def blog_profile(request, username):
    # Fetch the user or return 404 if not found
    profile_user = get_object_or_404(User, username=username)

    # Get blogs (exact match on username)
    blogs_by_author = Blog.objects.filter(author__username=username)

    # Get optional profile picture & bio
    profilepic = ProfilePic.objects.filter(user__username=username).first()
    bio = Profile.objects.filter(user__username=username).first()

    # For Users to update their profiles
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)
        if request.user != profile_user:
            return HttpResponseForbidden('Only the owner of this profile will be able to edit his details.')
        
        if form.is_valid():
            pfp = form.save(commit=False)
            pfp.user = request.user
            pfp.save()
            return redirect('blog_profile',username=request.user.username)
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        bio_text = request.POST.get('bio', '')


            
        profile_user.first_name = first_name
        profile_user.last_name = last_name
        profile_user.email = email
        profile_user.save()



        bio_instance, created = Profile.objects.get_or_create(user=profile_user)
        bio_instance.bio = bio_text
        bio_instance.save()


        return redirect('blog_profile',username=profile_user.username)
    else:
        form = ProfilePicForm()

    print(getattr(profile_user,'profilepic',None))
    # Render in one go — no branching needed
    return render(request, 'blog/profile.html', {
        'username': username,
        'profile_user': profile_user,
        'profilepic': profilepic,
        'form':form,
        'blogs_by_author': blogs_by_author if blogs_by_author.exists() else None,
        'bio': bio
    })


def blog_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        user_msg = Messages.objects.create(name=name,email=email,message=message)

        messages.success(request, "Your message has been sent successfully!")
        return redirect('blog_contact')
    return render(request, 'blog/contact.html', {})
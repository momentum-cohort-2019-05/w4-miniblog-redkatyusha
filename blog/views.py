from django.shortcuts import render

# Create your views here.

from blog.models import BlogPost, Blogger

def index(request):
    num_posts = BlogPost.objects.all().count()
    num_bloggers = Blogger.objects.count()

    context = {
        'num_posts': num_posts,
        'num_bloggers': num_bloggers,
    }

    return render(request, 'index.html', context=context)
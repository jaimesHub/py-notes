from django.shortcuts import render
from django.http import HttpResponse

"""dummy blog post data
    django template tutorial
    Returns:
        _type_: [post]
"""
posts = [
    {
        "title": "Beautiful is better than ugly",
        "author": "John Doe",
        "content": "Beautiful is better than ugly",
        "published_at": "January 15, 2024"
    },
    {
        "title": "Explicit is better than implicit",
        "author": "Jane Doe",
        "content": "Explicit is better than implicit",
        "published_at": "January 15, 2024"
    },
]

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Blog Home</h1>")
    
    # django-templates tut
    context = {
        "posts": posts,
        "title": "Zen of Python"
    }
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse("<h1>About</h1>")
    return render(request, 'blog/about.html') # django-templates tut
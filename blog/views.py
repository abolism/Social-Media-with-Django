from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# posts = [
#     {
#         'author': 'John Doe',
#         'title': 'Blog post 1',
#         'date': 'may 12, 2022',
#         'content': 'first post content'
#     }
#     ,
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog post 2',
#         'date': 'may 13, 2022',
#         'content': 'second post content'
#     }
# ]

def home(request):
    context ={'posts': Post.objects.all()}
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, "blog/home.html", context)

def about(request):
    context = {'title': 'About'}
    return render(request, "blog/about.html", context)


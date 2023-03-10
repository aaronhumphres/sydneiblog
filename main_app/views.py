from django.shortcuts import render
from .models import Post

# Define the home view
def home(request):
  posts = Post.objects.all()
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html', {'posts' : posts})

# about route
def about(request):
    return render(request, 'about.html')

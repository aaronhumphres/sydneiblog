from django.shortcuts import render

from blog.models import Post


# Define the home view
def homepage(request):
  posts = Post.objects.all()
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'main/homepage.html', {'posts' : posts})

# about route
def about(request):
    return render(request, 'main/about.html')

def trails(request):
    return render(request, 'main/trails.html')


   

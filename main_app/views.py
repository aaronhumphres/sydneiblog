from django.shortcuts import render, redirect
from .forms import CommentForm
from blog.models import Post


# Define the home view
def homepage(request):
  posts = Post.objects.all()
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'main/homepage.html', {'posts' : posts})

# about route
def about(request):
    return render(request, 'main/about.html')

def detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail', slug=post.slug)
    else:
        form = CommentForm()


    return render(request, 'main/detail.html', {'post': post, 'form': form,})
   

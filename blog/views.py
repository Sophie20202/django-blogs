from django.shortcuts import redirect, render

from blog.forms import BlogForm
from blog.models import Post

# Create your views here.

def create_post(request):
    form = BlogForm()
    context = {
        "form": form,
    }
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
        else:
            context = {
                "form": form,
                "errors": form.errors,
            }
        return render(request, 'create.html', context)
    return render(request, 'create.html', context)

def blog_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, 'index.html', context)
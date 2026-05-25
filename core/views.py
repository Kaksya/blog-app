from django.shortcuts import render, redirect
from .models import Blog


def blog_list(request):
    posts = Blog.objects.all().order_by("-created_at")

    return render(request, "blog.html", {"page": "list", "posts": posts})


def blog_detail(request, id):
    post = Blog.objects.filter(id=id).first()

    if post:
        post.views += 1
        post.save()

    return render(request, "blog.html", {"page": "detail", "post": post})


def add_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        video = request.FILES.get("video")

        Blog.objects.create(title=title, content=content, image=image, video=video)

        return redirect("blog_list")

    return render(request, "blog.html", {"page": "add"})


def about(request):
    return render(request, "blog.html", {"page": "about"})

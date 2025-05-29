from django.shortcuts import redirect, render
from News_app.models import Post

# Create your views here.
def post_list(request):
  Posts=Post.objects.filter(published_at_isnull=False).order_by("-published_at")
  return render(
    request,"post_list.html",{"posts":Posts}
  )



def post_detail(request,pk):
  post=Post.objects.get(pk=pk,published_at__isnull=False)
  return render(
    request,
    "post_detail.html",
    {"post":post}
  )


def draft_list(request):
  Posts=Post.objects.filter(published_at__isnull=True).order_by("-published_at")
  return render(
    request,
    "draft_list.html",
    {"posts":Posts}

  )


def draft_detail(request,pk):
  post=Post.objects.get(pk=pk,published_at_isnull=True)
  return render(
    request,
    "draft_detail.html",
    {"post":post}

  )


def post_delete(request,pk):
  post=Post.objects.get(pk=pk)
  post.delete()
  return redirect("post-list")
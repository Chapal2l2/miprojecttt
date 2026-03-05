
from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

def home(request):
    posts=Post.objects.all().order_by('-created_at')

    if request.method=='POST' and request.user.is_authenticated:
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('/')
    else:
        form=PostForm()

    return render(request,'posts/home.html',{'posts':posts,'form':form})

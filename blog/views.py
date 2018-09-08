from django.shortcuts import render, redirect
from .forms import PostForm

from django.utils import timezone
# Create your views here.

def postGate(request):

    return render(request, 'blog/index.html',{}) 

def postNew(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print("post method")###
        print(repr(form.fields))####
        
        if form.is_valid():
            print("post valid")###
            post = form.save(commit=False)
            post.author = request.user
            post.publishedDate = timezone.now()
            post.save()
            return redirect('postGate')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' :form })
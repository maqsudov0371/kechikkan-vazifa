from django.shortcuts import render
from .models import Category, Post

def blog(request):
    categoryes = Category.objects.all()
    posts = Post.objects.all()
    # banner = Banner.objects.last()
    return render(request,
                  'index.html',
                  context={
                           "categoryes": categoryes,
                           
                           })

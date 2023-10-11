from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post #把models.py已設好的東西匯入
from datetime import datetime

# Create your views here.
def homepage(request):
    posts=Post.objects.all()
    now=datetime.now()
    return render(request,'index.html',locals())

def showpost(request,slug):
    post=Post.objects.get(slug=slug)
    return render(request,'post.html',locals())

'''
def homepage(request):
    posts=Post.objects.all() #select * from post
    post_lists=list()
    for counter,post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_lists)
'''
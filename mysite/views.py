from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post #把models.py已設好的東西匯入
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    posts=Post.objects.all()
    now=datetime.now()
    return render(request,'index.html',locals())

def showpost(request,slug):
    try:
        post=Post.objects.get(slug=slug)
        if post !=None:
            return render(request,'post.html',locals())
        else:
            return redirect("/")
    except:
        return redirect("/")    

'''
def homepage(request):
    posts=Post.objects.all() #select * from post
    post_lists=list()
    for counter,post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_lists)
'''
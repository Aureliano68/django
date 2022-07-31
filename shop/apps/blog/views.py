from django.conf import settings
from django.shortcuts import render
from .models import author
from django.http import Http404
# Create your views here.

# def blog1(request):
#     auth1=AUTHOR(name='sajad',family='taheri',age=30)
#     author_add=auth1.save()
#     authors=AUTHOR.objects.all()
#     contex={
#         'author':authors
        
#     }
#     return render(request,'blog/page2.html',contex)


def blog1(request):
    media_urls=settings.MEDIA_URL
    contex={
        'media_url': media_urls,
        'imagename':'sci-search.jpg'
    }
    return render(request,'blog/page2.html',contex)
 


def author1(request):
    authors=author.objects.all()
    media_urls=settings.MEDIA_URL
    contex={
        'media_url': media_urls,
        'authors':authors
    }
    return render(request,'blog/page3.html',contex)


def author2(request):
 
    authors=author.objects.get(id=2)
    contex={
        'author':authors
    }
    return render(request,'blog/page_detail.html',contex)

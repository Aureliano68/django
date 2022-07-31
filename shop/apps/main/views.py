from django.conf import settings
from django.shortcuts import render

# Create your views here.

def main1(request):
    media_urls=settings.MEDIA_URL
    contex={
        'media_url':media_urls,
        
    }
    return render(request,'main/page1.html',contex)

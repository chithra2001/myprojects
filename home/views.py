from django.shortcuts import render
from lessor.models import *
from projectadmin.models import *
# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact-us.html')


def gallery(request):
    pon=pond_tb.objects.all()
    feed=Fishfeeds.objects.all()
    return render(request,'gallery.html',{'pon':pon,'feed':feed})

def about(request):
    return render(request,'about.html')
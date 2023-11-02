from django.shortcuts import render,redirect
from .models import *
from farmer.models import *
from user.models import *
from lessor.models import *
from django.contrib import messages
# Create your views here.

def areg(request):
    if request.method=="POST":
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        RePassword=request.POST.get('CPassword')
        if Password==RePassword:
            if projectadmin.objects.filter(Email=Email).exists():
                messages.info(request,'Email Address Already Exits')
            else:
                reg=projectadmin(Email=Email,Password=Password)
                reg.save()
                # print("values uploaded")
                return redirect('alog')
    
    return render(request,'admin/aregister.html')

def alog(request):
    error_message= None
    if request.method=="POST":
        try:
            Email=request.POST.get('Email')
            Password=request.POST.get('Password')
            log=projectadmin.objects.get(Email=Email,Password=Password)
            # if log.accept:
            request.session['Email']=log.Email
            request.session['id']=log.id

            return redirect('ahome')
            # else
                # messages.info(request,'Account Blocked')
        except projectadmin.DoesNotExist as e:
            messages.info(request,'Invalid User')

    return render(request,'admin/alogin.html',{'error':error_message})

def ahome(request):
    return render(request,'admin/ahome.html')

def addfish(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        reg=fishes(fname=fname)
        reg.save()
        # print("values uploaded")
        return redirect('ahome')
    return render(request,'admin/addfishes.html')

def addfeed(request):
    if request.method=="POST":
        feedname=request.POST.get('feedname')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        img=request.FILES.get('img')
        description=request.POST.get('description')
        reg=Fishfeeds(feedname=feedname,quantity=quantity,
                      price=price,img=img,description=description)
        reg.save()
        # print("values uploaded")
        return redirect('ahome')
    return render(request,'admin/addfeed.html')


def tables(request):
    far=f_reg.objects.all()
    return render(request,'admin/table.html',{'far':far})

def tables1(request):
    les=l_reg.objects.all()
    return render(request,'admin/table1.html',{'les':les})

def tables2(request):
    pro=u_reg.objects.all()
    return render(request,'admin/table2.html',{'pro':pro})




def faccept(request,id):
    f_reg.objects.filter(id=id).update(accept=True)
    return redirect('ahome')


def freject(request,id):
    pro=f_reg.objects.filter(id=id)
    pro.delete()
    return redirect('ahome')

#def fishaccept(request,id):
 #   product_tb.objects.filter(id=id).update(accept=True)
 #   return redirect('vfish')


#def fishreject(request,id):
 #   pro=product_tb.objects.filter(id=id)
  #  pro.delete()
   # return redirect('vfish')


def vfish(request):
    pro=product_tb.objects.all()
    return render(request,'admin/viewfishes.html',{'pro':pro})

def viewpond(request):
    pro=pond_tb.objects.all()
    return render(request,'admin/viewfarmingponds.html',{'pro':pro})

def ponddel(request,id):
    pro=pond_tb.objects.filter(id=id)
    pro.delete()
    return redirect('viewpond')

def vfeed(request):
    pro=Fishfeeds.objects.all()
    return render(request,'admin/viewfeed.html',{'pro':pro})



def bookdtls(request):
    
    pros=book_feed.objects.all()
    return render(request,'admin/bookdetails.html',{'pros':pros})

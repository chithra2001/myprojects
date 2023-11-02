from django.shortcuts import render,redirect
from .models import *
from projectadmin.models import *
from lessor.models import *
from user.models import *

from django.contrib import messages
import os

from mariculture.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
# Create your views here.

def freg(request):
    if request.method=="POST":
        F_name=request.POST.get('F_name')
        License_id=request.POST.get('License_id')
        House_name=request.POST.get('House_name')
        Street=request.POST.get('Street')
        District=request.POST.get('District')
        State=request.POST.get('State')
        Pincode=request.POST.get('Pincode')
        Phoneno=request.POST.get('Phoneno')
        whatsappno=request.POST.get('whatsappno')
        Email=request.POST.get('Email')
        Gender=request.POST.get('Gender')
        Experience=request.POST.get('Experience')
        Password=request.POST.get('Password')
        RePassword=request.POST.get('CPassword')
        if Password==RePassword:
            if f_reg.objects.filter(Phoneno=Phoneno).exists():
                messages.info(request,'PhoneNumber Already Exits')
            elif f_reg.objects.filter(Email=Email).exists():
                messages.info(request,'Email Address Already Exits')
            else:
                reg=f_reg(F_name=F_name,Gender=Gender,Email=Email,Phoneno=Phoneno,whatsappno=whatsappno,License_id=License_id,House_name=House_name,
                          Street=Street,District=District,State=State,Pincode=Pincode,Password=Password,Experience=Experience)
                reg.save()
                # print("values uploaded")
                return redirect('flog')
    
    return render(request,'farmer/fregister.html')

def flog(request):
    error_message= None
    if request.method=="POST":
        try:
            Email=request.POST.get('Email')
            Password=request.POST.get('Password')
            log=f_reg.objects.get(Email=Email,Password=Password)
            if log.accept:
                request.session['F_name']=log.F_name
                request.session['id']=log.id

                return redirect('fhome')
            else:
                messages.info(request,'Account Blocked')
        except f_reg.DoesNotExist as e:
            messages.info(request,'Invalid User')

    return render(request,'farmer/flogin.html',{'error':error_message})

def fhome(request):
    id=request.session['id']
    pro=f_reg.objects.get(id=id)
    return render(request,'farmer/fhome.html',{'pro':pro})



def addfish(request):
    pro=fishes.objects.all()
    if request.method=="POST":
        P_name=request.POST.get('P_name')
        Fid=request.session['id']
        p_type=request.POST.get('p_type')
        Grade=request.POST.get('Grade')
        p_img=request.FILES.get('p_img')
        avgwght=request.POST.get('avgwght')
        upld_date=request.POST.get('upld_date')
        upld_time=request.POST.get('upld_time')
        price=request.POST.get('price')
        Description=request.POST.get('Description')
        reg=product_tb(P_name=P_name,Fid_id=Fid,p_type=p_type,Grade=Grade,p_img=p_img,avgwght=avgwght,
                  upld_date=upld_date,upld_time=upld_time,price=price,Description=Description)
        reg.save()
        # print("values uploaded")
        return redirect('viewfish')
    
    return render(request,'farmer/addfishes.html',{'pro':pro})



def viewfish(request):
    id=request.session['id']
    pro=product_tb.objects.filter(Fid=id)
    return render(request,'farmer/viewfish.html',{'pro':pro})




def delfish(request,id):
    fish=product_tb.objects.get(id=id)
    fish.delete()
    return redirect('viewfish')

def editproduct(request,id):
    edit=product_tb.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(edit.p_img)>0:
                os.remove(edit.p_img.path)
            edit.p_img=request.FILES["Image"]    
        edit.price = request.POST.get('price')
        edit.avgwght = request.POST.get('avgwght')
        edit.Description = request.POST.get('Description')
        edit.save()
        return redirect('fhome')
    return render(request,"farmer/editfish.html",{"edit":edit})

def vpond(request):
    pro=pond_tb.objects.all()
    return render(request,'farmer/viewpond.html',{'pro':pro})

def fmap(request,id):
    pro=pond_tb.objects.get(id=id)
    return render(request,'farmer/fmap.html',{'pro':pro})

def forder(request):
    id=request.session['id']
    fa=f_reg.objects.get(id=id)
    far=fa.F_name
    pro=book_f.objects.filter(farmer=far)
    pros=h_book.objects.filter(pid__Fid=id)
    return render(request,'farmer/fishorder.html',{'pro':pro,'pros':pros})
    


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))




def fprofile(request):
    id=request.session['id']
    pro=f_reg.objects.get(id=id)
    return render(request,'farmer/fprofile.html',{'pd':pro})

def feditpro(request,id):
    edit=f_reg.objects.get(id=id)
    if request.method=="POST":
        edit.F_name=request.POST.get('F_name')
        edit.License_id=request.POST.get('License_id')
        edit.Experience=request.POST.get('Experience')
        edit.House_name=request.POST.get('House_name')
        edit.Street=request.POST.get('Street')
        edit.Pincode=request.POST.get('Pincode')
        edit.Phoneno=request.POST.get('Phoneno')
        edit.Email=request.POST.get('Email')
        edit.Password=request.POST.get('Password')
        edit.save()
        return redirect("fprofile")
    return render(request,'farmer/feditpro.html',{'pro':edit})

def vfeed(request):
    id=request.session['id']
    pro=Fishfeeds.objects.all()
    return render(request,'farmer/viewfeed.html',{'pro':pro})

def bookfeed(request,id):
    pro=Fishfeeds.objects.get(id=id)
    if request.method=="POST":
        feedname=request.POST.get('feedname')
        quantity=request.POST.get('quantity')
        packets=request.POST.get('packets')
        price=request.POST.get('price')


        total=int(price)*int(packets)
        fid=request.session['id']
        reg=book_feed(feedname=feedname,quantity=quantity,packets=packets,price=price,total=total,
                      fid_id=fid,book=True)
        reg.save()
        # print("values uploaded")
        return redirect('cart')
    
    return render(request,'farmer/bfeed.html',{'pro':pro})

def ordertb(request):
    id=request.session['id']
    pro=book_feed.objects.filter(fid=id)
    return render(request,'farmer/ordertb.html',{'pro':pro})





def cart(request):
    id=request.session['id']
    menu=book_feed.objects.filter(fid=id,payment=False)
    global amount
    sum=0  
    amount=0     
    for i in menu:
            sum += float(i.price) * int(i.packets)
            amount=sum
    return render(request,'farmer/cart.html',{'menu':menu,'sum':sum,'amount':amount})


    
def fremove(request,id):
    pro=book_feed.objects.get(id=id)
    pro.delete()
    return redirect('cart')

def ordremove(request,id):
    rem=book_feed.objects.filter(id=id)
    re=rem.delete()
    return redirect('ordertb')


def viewpond(request):
    pro=pond_tb.objects.all()
    return render(request,'farmer/viewpond.html',{'pro':pro})

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))


def feedpay(request):
    global amount
    id=request.session['id']
    book_feed.objects.filter(fid=id).update(payment=True)
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    
    return render(request,'farmer/feedpay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})



def feedbill(request):
    id=request.session['id']
    pro=book_feed.objects.filter(fid=id)
    sum=0  
    for i in pro:
            sum += float(i.price) * int(i.packets)
    return render(request,'farmer/bill.html',{'pro':pro,'sum':sum})



def salesreport(request):
    if request.method=="POST":
        startdate=request.POST.get('startdate')
        enddate=request.POST.get('enddate')
        sales=book_f.objects.filter(billdate__range=[startdate,enddate])
        sum=0
        for i in sales:
            sum += i.total
    
        return render(request,'farmer/salesrep.html',{'startdate':startdate,'enddate':enddate,'sales':sales,'sales_json':sales,'sum':sum})
    
    return render(request,'farmer/report.html')

def useraccp(request,id):
    book_f.objects.filter(id=id).update(accept=True)
    book_f.objects.filter(id=id).update(reject=False)
    return redirect('forder')


def userrej(request,id):
    book_f.objects.filter(id=id).update(accept=False)
    book_f.objects.filter(id=id).update(reject=True)
    return redirect('forder')


def hotelaccp(request,id):
    h_book.objects.filter(id=id).update(accept=True)
    h_book.objects.filter(id=id).update(reject=False)
    return redirect('forder')


def hotelrej(request,id):
    h_book.objects.filter(id=id).update(accept=False)
    h_book.objects.filter(id=id).update(reject=True)
    return redirect('forder')
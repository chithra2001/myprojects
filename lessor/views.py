from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from mariculture.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
# Create your views here.

def lreg(request):
    if request.method=="POST":
        L_name=request.POST.get('L_name')
        House_name=request.POST.get('House_name')
        Street=request.POST.get('Street')
        District=request.POST.get('District')
        State=request.POST.get('State')
        Pincode=request.POST.get('Pincode')
        Phoneno=request.POST.get('Phoneno')
        Email=request.POST.get('Email')
        Gender=request.POST.get('Gender')
        Password=request.POST.get('Password')
        RePassword=request.POST.get('CPassword')
        if Password==RePassword:
            if l_reg.objects.filter(Phoneno=Phoneno).exists():
                messages.info(request,'PhoneNumber Already Exits')
            elif l_reg.objects.filter(Email=Email).exists():
                messages.info(request,'Email Address Already Exits')
            else:
                reg=l_reg(L_name=L_name,Gender=Gender,Email=Email,Phoneno=Phoneno,House_name=House_name,
                          Street=Street,District=District,State=State,Pincode=Pincode,Password=Password)
                reg.save()
                # print("values uploaded")
                return redirect('Llog')
    
    return render(request,'lessor/lregister.html')

def Llog(request):
    error_message= None
    if request.method=="POST":
        try:
            Email=request.POST.get('Email')
            Password=request.POST.get('Password')
            log=l_reg.objects.get(Email=Email,Password=Password)
            # if log.accept:
            request.session['L_name']=log.L_name
            request.session['id']=log.id

            return redirect('lhome')
            # else
                # messages.info(request,'Account Blocked')
        except l_reg.DoesNotExist as e:
            messages.info(request,'Invalid User')

    return render(request,'lessor/Llogin.html',{'error':error_message})

def lhome(request):
    id=request.session['id']
    pro=l_reg.objects.get(id=id)
    return render(request,'lessor/lhome.html',{'pro':pro})

def addpond(request):
    if request.method=="POST":
        type=request.POST.get('type')
        district=request.POST.get('district')
        loc=request.POST.get('loc')
        cent=request.POST.get('cent')
        price=request.POST.get('price')
        Lid=request.session['id']
        phoneno=request.POST.get('phoneno')
        Description=request.POST.get('Description')
        pond_img=request.FILES.get('pond_img')
        reg=pond_tb(type=type,district=district,loc=loc,cent=cent,price=price,Lid_id=Lid,phoneno=phoneno,Description=Description,pond_img=pond_img)
        reg.save()
        # print("values uploaded")

        return redirect('PondDet')
    
    return render(request,'lessor/addponds.html')


def PondDet(request):
    id=request.session['id']
    pro=pond_tb.objects.filter(Lid=id)
    return render(request,'lessor/PondDet.html',{'pr':pro})


def remove(request,id):
    pro=pond_tb.objects.filter(Lid=id)
    pro.delete()
    return redirect('PondDet')

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def pondpay(request,id):
    global amount
    data=pond_tb.objects.get(id=id)
    pond_tb.objects.filter(id=id).update(ppayment=True)
    pond_tb.objects.filter(id=id).update(pstatus=False)
    amount=6000
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'lessor/pondpay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})


def vpond(request):
    id=request.session['id']
    pro=pond_tb.objects.filter(Lid=id)
    return render(request,'lessor/viewpond.html',{'pro':pro})

def lprofile(request):
    id=request.session['id']
    pro=l_reg.objects.get(id=id)
    return render(request,'lessor/lprofile.html',{'pd':pro})

def leditpro(request,id):
    edit=l_reg.objects.get(id=id)
    if request.method=="POST":
        edit.L_name=request.POST.get('L_name')
        edit.House_name=request.POST.get('House_name')
        edit.Street=request.POST.get('Street')
        edit.Pincode=request.POST.get('Pincode')
        edit.Phoneno=request.POST.get('Phoneno')
        edit.Email=request.POST.get('Email')
        edit.Password=request.POST.get('Password')
        edit.save()
        return redirect("lprofile")
    return render(request,'lessor/leditpro.html',{'pro':edit})

def editpond(request,id):
    edit=pond_tb.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(edit.p_img)>0:
              
             edit.pond_img=request.FILES["Image"]    
        edit.price = request.POST.get('price')
        edit.Description = request.POST.get('Description')
        edit.save()
        return redirect('vpond')
    return render(request,"lessor/editpond.html",{"edit":edit})

def delpond(request,id):
    pond=pond_tb.objects.get(id=id)
    pond.delete()
    return redirect('vpond')


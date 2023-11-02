from django.shortcuts import render,redirect
from .models import *
from farmer.models import *
from lessor.models import *
from django.contrib import messages
from django.db.models import Q
from datetime import datetime,date
from mariculture.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
# Create your views here.
def ureg(request):
    if request.method=="POST":
        U_name=request.POST.get('U_name')
        House_name=request.POST.get('House_name')
        Street=request.POST.get('Street')
        District=request.POST.get('District')
        State=request.POST.get('State')
        Pincode=request.POST.get('Pincode')
        Phoneno=request.POST.get('Phoneno')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        RePassword=request.POST.get('CPassword')
        if Password==RePassword:
            if u_reg.objects.filter(Phoneno=Phoneno).exists():
                messages.info(request,'PhoneNumber Already Exits')
            elif u_reg.objects.filter(Email=Email).exists():
                messages.info(request,'Email Address Already Exits')
            else:
                reg=u_reg(U_name=U_name,House_name=House_name,Street=Street,District=District,State=State,Pincode=Pincode,
                          Phoneno=Phoneno,Email=Email,Password=Password)
                reg.save()
                # print("values uploaded")
                return redirect('ulog')
    
    return render(request,'user/uregister.html')

def hreg(request):
    if request.method=="POST":
        Name=request.POST.get('Name')
        Street=request.POST.get('Street')
        District=request.POST.get('District')
        State=request.POST.get('State')
        Pincode=request.POST.get('Pincode')
        Phoneno=request.POST.get('Phoneno')
        Photo=request.FILES.get('Photo')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        RePassword=request.POST.get('CPassword')

        if Password==RePassword:
            if h_reg.objects.filter(Phoneno=Phoneno).exists():
                messages.info(request,'PhoneNumber Already Exits')
            elif h_reg.objects.filter(Email=Email).exists():
                messages.info(request,'Email Address Already Exits')
            else:
                reg=h_reg(Name=Name,Street=Street,District=District,State=State,Pincode=Pincode,
                          Photo=Photo,Phoneno=Phoneno,Email=Email,Password=Password)
                reg.save()
                # print("values uploaded")
                return redirect('hlog')
    
    return render(request,'user/hotelreg.html')

def ulog(request):
    error_message= None
    if request.method=="POST":
        try:
            Email=request.POST.get('Email')
            Password=request.POST.get('Password')
            log=u_reg.objects.get(Email=Email,Password=Password)
            # if log.accept:
            request.session['U_name']=log.U_name
            request.session['id']=log.id

            return redirect('uhome')
            # else
                # messages.info(request,'Account Blocked')
        except u_reg.DoesNotExist as e:
            messages.info(request,'Invalid User')

    return render(request,'user/ulogin.html',{'error':error_message})

def hlog(request):
    error_message= None
    if request.method=="POST":
        try:
            Email=request.POST.get('Email')
            Password=request.POST.get('Password')
            log=h_reg.objects.get(Email=Email,Password=Password)
            # if log.accept:
            request.session['Name']=log.Name
            request.session['id']=log.id

            return redirect('hhome')
            # else
                # messages.info(request,'Account Blocked')
        except h_reg.DoesNotExist as e:
            messages.info(request,'Invalid User')

    return render(request,'user/hotlog.html',{'error':error_message})


def uhome(request):
    id=request.session['id']
    pro=u_reg.objects.get(id=id)
    return render(request,'user/uhome.html',{'pro':pro})

def hhome(request):
    return render(request,'user/hhome.html')

def vcatla(request):
    pro=product_tb.objects.filter(P_name="Catla")
    return render(request,'user/viewfish.html',{'pro':pro})

def vkarimeen(request):
    pro=product_tb.objects.filter(P_name="Karimeen")
    return render(request,'user/viewfish.html',{'pro':pro})

def vmushi(request):
    pro=product_tb.objects.filter(P_name="Mushi")
    return render(request,'user/viewfish.html',{'pro':pro})

def vrohu(request):
    pro=product_tb.objects.filter(P_name="Rohu")
    return render(request,'user/viewfish.html',{'pro':pro})

def vprawns(request):
    pro=product_tb.objects.filter(P_name="Prawns")
    return render(request,'user/viewfish.html',{'pro':pro})

def vvaala(request):
    pro=product_tb.objects.filter(P_name="vaala")
    return render(request,'user/viewfish.html',{'pro':pro})

def vvaraal(request):
    pro=product_tb.objects.filter(P_name="Varaal")
    return render(request,'user/viewfish.html',{'pro':pro})

def vnutter(request):
    pro=product_tb.objects.filter(P_name="nutter")
    return render(request,'user/viewfish.html',{'pro':pro})

def vthilopia(request):
    pro=product_tb.objects.filter(P_name="Thilopia")
    return render(request,'user/viewfish.html',{'pro':pro})

def vkaari(request):
    pro=product_tb.objects.filter(P_name="Kaari")
    return render(request,'user/viewfish.html',{'pro':pro})

def vchempally(request):
    pro=product_tb.objects.filter(P_name="Chempally")
    return render(request,'user/viewfish.html',{'pro':pro})

def vparal(request):
    pro=product_tb.objects.filter(P_name="Paral")
    return render(request,'user/viewfish.html',{'pro':pro})

def vpallathi(request):
    pro=product_tb.objects.filter(P_name="Pallathi")
    return render(request,'user/viewfish.html',{'pro':pro})

def vkanambu(request):
    pro=product_tb.objects.filter(P_name="Kanambu")
    return render(request,'user/viewfish.html',{'pro':pro})

def vpullan(request):
    pro=product_tb.objects.filter(P_name="Pullan")
    return render(request,'user/viewfish.html',{'pro':pro})

def vfishcate(request):
    return render(request,'user/vfishcate.html')

def viewfishcate(request):
    return render(request,'user/viewfishcate.html')

# def hcatla(request):
#     pros=product_tb.objects.filter(Q(P_name = "Catla") | Q(P_name = "catla"))
#     prof = list(pros.values_list('Fid', flat=True))
#     pro = f_reg.objects.filter(id__in=prof)

#     return render(request,'user/farmer.html',{'pro':pro})

def hcatla(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="Catla").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request, 'user/farmer.html', {'pro': pro})


def hkarimeen(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="Karimeen").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hrohu(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="rohu").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hmushi(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="mushi").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hprawns(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="prawns").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hvaala(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="vaala").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hvaraal(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="varaal").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hnutter(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="nutter").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hthilopia(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="thilopia").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hkaari(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="kaari").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hchempally(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="chempally").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hparal(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="paral").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hpallathi(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="pallathi").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hkanambu(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="kanambu").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hpullan(request):

    ids = set()
    pro = []
    prof=product_tb.objects.filter(P_name__iexact="pullan").filter(Q(Description__icontains="uncleaned") | Q(Description__icontains="not cleaned"))

    for prod in prof:
        if prod.Fid not in ids:
            ids.add(prod.Fid)
            pro.append(prod)

    return render(request,'user/farmer.html',{'pro':pro})

def hotelbook(request,id):
    pro=product_tb.objects.get(id=id)
    day=date.today().strftime('%Y-%m-%d')
    if request.method=="POST":
        P_name=request.POST.get('P_name')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        hid=request.session['id']
        pid=id
        total=int(price)*int(quantity)
        del_date=request.POST.get('del_date')
        reg=h_book(P_name=P_name,quantity=quantity,price=price,hid_id=hid,
                   del_date=del_date,book=True,pid_id=pid,total=total)
        reg.save()
        return redirect('vhbook')
    return render(request,'user/bhotelfish.html',{'pro':pro,'day':day})

def vhbook(request):
    id=request.session['id']
    pro=h_book.objects.filter(hid=id)
    return render(request,'user/vhbook.html',{'pro':pro})

def hbookrem(request,id):
    rem=h_book.objects.filter(id=id)
    rem.delete()
    return redirect('vhbook')


def hotelpay(request,id):
    global amount
    data=h_book.objects.get(id=id)
    h_book.objects.filter(id=id).update(payment=True)
    amount=data.total
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'user/hotelpay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

def hotelbill(request,id):
    pro=h_book.objects.get(id=id)
    return render(request,'user/hotelbill.html',{'pro':pro})


def viewpond(request):
    pro=pond_tb.objects.all()
    return render(request,'user/viewpond.html',{'pro':pro})

def umap(request,id):
    pro=pond_tb.objects.get(id=id)
    return render(request,'user/umap.html',{'pro':pro})

def bookf(request,id):
    pro=product_tb.objects.get(id=id)
    if request.method=="POST":
        P_name=request.POST.get('P_name')
        farmer=request.POST.get('farmer')
        avgwght=request.POST.get('avgwght')
        Grade=request.POST.get('Grade')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        total=int(price)*int(quantity)
        Uid=request.session['id']
        del_date=request.POST.get('del_date')
        del_time=request.POST.get('del_time')
        reg=book_f(P_name=P_name,farmer=farmer,avgwght=avgwght,Grade=Grade,quantity=quantity,total=total,price=price,Uid_id=Uid,
                   del_date=del_date,del_time=del_time,book=True)
        reg.save()
        # print("values uploaded")
        return redirect('booking')
    
    return render(request,'user/bfish.html',{'pro':pro})




def uremove(request,id):
    rem=book_f.objects.filter(id=id)
    re=rem.delete()
    return redirect('booking')


def booking(request):
    id=request.session['id']
    pro=book_f.objects.filter(Uid=id)
    # i=book_f.objects.get(Uid=id)
    sum=0 
    # sum +=i.price * i.quantity
    global amount
    amount=sum

    pros=book_f.objects.filter(Uid=id)

    return render(request,'user/booking.html',{'pro':pro,'sum':sum,'amount':amount,'pros':pros})


client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def fishpay(request,id):
    global amount
    data=book_f.objects.get(id=id)
    book_f.objects.filter(id=id).update(payment=True)
    amount=data.total
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'user/fishpay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})





def uprofile(request):
    id=request.session['id']
    pro=u_reg.objects.get(id=id)
    return render(request,'user/uprofile.html',{'pd':pro})

def ueditpro(request,id):
    edit=u_reg.objects.get(id=id)
    if request.method=="POST":
        edit.U_name=request.POST.get('U_name')
        edit.House_name=request.POST.get('House_name')
        edit.Street=request.POST.get('Street')
        edit.Pincode=request.POST.get('Pincode')
        edit.Phoneno=request.POST.get('Phoneno')
        edit.Email=request.POST.get('Email')
        edit.Password=request.POST.get('Password')
        edit.save()
        return redirect("uprofile")
    return render(request,'user/ueditpro.html',{'pro':edit})


def hotelprof(request):
    id=request.session['id']
    pro=h_reg.objects.get(id=id)
    return render(request,'user/hprofile.html',{'pd':pro})

def heditpro(request,id):
    edit=h_reg.objects.get(id=id)
    if request.method=="POST":
        edit.Name=request.POST.get('Name')
        edit.Street=request.POST.get('Street')
        edit.Pincode=request.POST.get('Pincode')
        edit.Phoneno=request.POST.get('Phoneno')
        edit.Email=request.POST.get('Email')
        edit.Password=request.POST.get('Password')
        edit.save()
        return redirect("hotelprof")
    return render(request,'user/heditprof.html',{'pro':edit})


#def pondpay(request,id):
#    global amount
    # data=book_f.objects.get(id=id)
    # pond_tb.objects.filter(id=id).update(payment=True)
 #   pro=pond_tb.objects.get(id=id)
  #  amount=pro.price
   # print(amount)
    #currency ="INR"
    #api_key=RAZORPAY_API_KEY
    #amt=int(amount)*100
    #payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    #payment_order_id= payment_order['id'] 

    # if request.method=="POST":
    #type=pro.type
    #location=pro.loc
    #Description=pro.Description
    #lessor=pro.Lid
    #breadth=pro.breadth
    #length=pro.length
    #price=pro.price
    #uid=request.session['id']
    #reg=book_p(type=type,location=location,desc=Description,lessor=lessor,
     #              length=length,breadth=breadth,price=price,Uid_id=uid,book=True,payment=True)
    #reg.save()

    #return render(request,'user/fishpay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

# def cart(request):
#     id=request.session['id']
#     menu=book_f.objects.filter(Uid=id,payment=False)
#     sum=0       
#     for i in menu:
#             sum +=i.price * i.quantity
#             global amount
#             amount=sum
#     return render(request,'user/cart.html',{'menu':menu,'sum':sum,'amount':amount})


#def bookp(request,id):
 #   pro=pond_tb.objects.get(id=id)
    # if request.method=="POST":
 #   type=pro.type
 #   location=pro.loc
 #   Description=pro.Description
 #   lessor=pro.Lid
 #   breadth=pro.breadth
 #   length=pro.length
 #   price=pro.price
 #   uid=request.session['id']
 #   reg=book_p(type=type,location=location,desc=Description,lessor=lessor,
  #                 length=length,breadth=breadth,price=price,Uid_id=uid,book=True)
 #   reg.save()
 #   return redirect('uhome')
    
    # return render(request,'user/uhome.html',{'pro':pro})




def frate(request,id):
    h=book_f.objects.get(id=id)
    if request.method=="POST":
        
        rate=request.POST['rate'] 
        review=request.POST['Suggestions']
        book_f.objects.filter(id=id).update(rate=rate)
        book_f.objects.filter(id=id).update(review=review)
        # data=rating.objects.get(Filmid=id)
        # pid=data.producerId
        # data=hotelrate.objects.filter(hotel=id)
        # length=len(data)
        # # trate=[]
        # x=0
        # for i in data:
        #     x=int(i.rate)+x
        
        # trate=int(round(x/length))
        # Hotel_reg.objects.filter(id=id).update(avgrate=trate)
        # Hotel_reg.objects.filter(id=id).update(rlength=length)
        return redirect('uhome')
    
    return render(request,'user/fishrate.html',{'h':h})


def bill(request,id):
    # id=request.session['id']
    pro=book_f.objects.get(id=id)
    return render(request,'user/bill.html',{'pro':pro})


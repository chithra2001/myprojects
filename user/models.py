from django.db import models
from django.utils import timezone 
from farmer.models import *
# Create your models here.
# Create your models here.
class u_reg(models.Model):
    U_name=models.CharField(max_length=20)
    House_name=models.CharField(max_length=50)
    Street=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Phoneno=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=20)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    

    def __str__(self) :
        return self.U_name
    
class h_reg(models.Model):
    Name=models.CharField(max_length=20)
    Street=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Phoneno=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to="hotel")
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    

    def __str__(self) :
        return self.Name

    

class book_f(models.Model):
    P_name=models.CharField(max_length=20)
    farmer=models.CharField(max_length=20)
    avgwght=models.CharField(max_length=20,null=True)
    Grade=models.CharField(max_length=20,null=True)
    quantity=models.IntegerField()
    price=models.IntegerField()
    billdate=models.DateTimeField(default=timezone.now)
    total=models.IntegerField()
    Uid=models.ForeignKey(u_reg,on_delete=models.CASCADE)
    del_date=models.CharField(max_length=50)
    del_time=models.CharField(max_length=50)
    payment=models.BooleanField(default=False)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    book=models.BooleanField(default=False)
    rate=models.CharField(max_length=20,null=True)
    review=models.CharField(max_length=20,null=True)
    
    
    

    def __str__(self) :
        return self.P_name  

#class book_p(models.Model):
   # type=models.CharField(max_length=20)
    #location=models.CharField(max_length=20,null=True)
    #desc=models.CharField(max_length=20,null=True)
    #lessor=models.CharField(max_length=20,null=True)
    #breadth=models.IntegerField()
    #length=models.IntegerField()
    #Uid=models.ForeignKey(u_reg,on_delete=models.CASCADE)
    #price=models.IntegerField()
    #payment=models.BooleanField(default=False)
    #accept=models.BooleanField(default=False)
    #reject=models.BooleanField(default=False)
    #book=models.BooleanField(default=False)
    
    
    

    #def __str__(self) :
     #   return self.type   

                  

# class fishrate(models.Model):
#     rate=models.CharField(max_length=20)
#     review=models.CharField(max_length=20)
#     Uid=models.ForeignKey(u_reg,on_delete=models.CASCADE)
#     book=models.ForeignKey(book_f,on_delete=models.CASCADE)
    
    

#     def __str__(self) :
#         return self.P_name  


class h_book(models.Model):
    P_name=models.CharField(max_length=20)
    quantity=models.FloatField()
    price=models.FloatField()
    total=models.IntegerField()
    billdate=models.DateTimeField(default=timezone.now)
    hid=models.ForeignKey(h_reg,on_delete=models.CASCADE)
    pid=models.ForeignKey(product_tb,on_delete=models.CASCADE)
    del_date=models.CharField(max_length=50)
    payment=models.BooleanField(default=False)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    book=models.BooleanField(default=False) 

    def __str__(self) :
        return self.P_name
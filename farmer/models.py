from django.db import models
from django.utils import timezone
# Create your models here.
class f_reg(models.Model):
    F_name=models.CharField(max_length=20)
    License_id=models.CharField(max_length=20)
    Experience=models.IntegerField()
    House_name=models.CharField(max_length=50)
    Street=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Phoneno=models.CharField(max_length=10)
    whatsappno=models.CharField(max_length=10,null=True)
    Email=models.CharField(max_length=50)
    Gender=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    

    def __str__(self) :
        return self.F_name

class product_tb(models.Model):
    P_name=models.CharField(max_length=20)
    p_type=models.CharField(max_length=20)
    Grade=models.CharField(max_length=20,null=True)
    p_img=models.ImageField(upload_to='product')
    Fid=models.ForeignKey(f_reg,on_delete=models.CASCADE)
    avgwght=models.CharField(max_length=50)
    upld_date=models.DateField('upld_date',null=True)
    upld_time=models.TimeField('upld_time',null=True)
    price=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    fpayment=models.BooleanField(default=False)
    fstatus=models.BooleanField(default=False)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    
    

    def __str__(self) :
        return self.P_name



class book_feed(models.Model):
    feedname=models.CharField(max_length=20)
    quantity=models.IntegerField()
    packets=models.IntegerField(null=True)
    price=models.IntegerField()
    total=models.IntegerField()
    billdate=models.DateTimeField(default=timezone.now)
    fid=models.ForeignKey(f_reg,on_delete=models.CASCADE)
    payment=models.BooleanField(default=False)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    book=models.BooleanField(default=False)
    
    

    def __str__(self) :
        return self.feedname
from django.db import models
from django.utils import timezone
# Create your models here.
class l_reg(models.Model):
    L_name=models.CharField(max_length=20)
    House_name=models.CharField(max_length=50)
    Street=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Phoneno=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    Gender=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    

    def __str__(self) :
        return self.L_name
    
class pond_tb(models.Model):   
    type=models.CharField(max_length=20)
    district=models.CharField(max_length=20,null=True)
    loc=models.CharField(max_length=20)
    cent=models.IntegerField(null=True)
    price=models.CharField(max_length=50)
    Lid=models.ForeignKey(l_reg,on_delete=models.CASCADE)
    phoneno=models.IntegerField(null=True)
    Description=models.CharField(max_length=5000)
    pond_img=models.ImageField(upload_to='pond')
    ppayment=models.BooleanField(default=False)
    pstatus=models.BooleanField(default=False)
    # preject=models.BooleanField(default=False)
    Adpr=models.CharField(max_length=20,null=True)
    date=models.DateField(default=timezone.now)
    

    def __str__(self) :
        return self.type
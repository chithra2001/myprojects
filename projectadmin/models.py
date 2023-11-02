from django.db import models

# Create your models here.
class projectadmin(models.Model):
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=20)
    

    def __str__(self) :
        return self.Email
    

class fishes(models.Model):
    fname=models.CharField(max_length=50)

    def __str__(self) :
        return self.fname
    
class Fishfeeds(models.Model):
    feedname=models.CharField(max_length=50,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    img=models.ImageField(upload_to="feed")
    description=models.CharField(max_length=500,null=True)





    def __str__(self) :
        return self.feedname    
    

    

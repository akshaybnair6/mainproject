from django.db import models
from django.contrib.auth.models import User
class UserReg(models.Model):
    username=models.CharField(max_length=250,null=True)
    password1 = models.CharField(max_length=250,blank=True,null=True)
    password2 = models.CharField(max_length=250,blank=True,null=True)
    location = models.CharField(max_length=250,null=True)
    email = models.CharField(max_length=250,null=True)
    phonenumber = models.CharField(max_length=225,null=True)
    def __str__(self):
        return self.username
class Vehicle(models.Model):

    # userid=models.ForeignKey('UserReg',related_name='userid',on_delete=models.CASCADE)

    brand=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='vehicle/uploads',default=None,blank=True)
    image1=models.ImageField(upload_to='vehicle/uploads',default=None,blank=True)
    image2=models.ImageField(upload_to='vehicle/uploads',default=None,blank=True)
    image3=models.ImageField(upload_to='vehicle/uploads',default=None,blank=True)
    description = models.TextField()

class VehicleDetails(models.Model):
    vuserid=models.ForeignKey('UserReg',related_name='vuserid',on_delete=models.CASCADE)
    vvehicleid=models.ForeignKey('Vehicle',related_name='vvehicleid',on_delete=models.CASCADE)
    # vbrand=models.CharField(max_length=50)
    # vmodel=models.CharField(max_length=50)
    # vyear = models.PositiveIntegerField()
    # vmileage = models.PositiveIntegerField()
    # vprice = models.DecimalField(max_digits=10, decimal_places=2)
    # vimage=models.ImageField(upload_to='vehicle/uploads',default=None,blank=True)
    # vimage1=models.ImageField(upload_to='vehicle/uploads',default=None,blank=True)
    # vimage2=models.ImageField(upload_to='vehicle/uploads',default=None,blank=True)
    # vimage3=models.ImageField(upload_to='vehicle/uploads',default=None,blank=True)
    
class Order(models.Model):
    vehicleid=models.ForeignKey('Vehicle',on_delete=models.CASCADE,related_name="distinctve")
    userid=models.ForeignKey('UserReg',related_name='comments',on_delete=models.CASCADE)
    dateordered=models.DateField()
class Favourites(models.Model):
    vehicleid=models.ForeignKey('Vehicle',on_delete=models.CASCADE)
    userid = models.ForeignKey('UserReg', on_delete=models.CASCADE)
class Addtocart(models.Model):
    vehicleid=models.ForeignKey('Vehicle',on_delete=models.CASCADE)
    
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
class Wishlist(models.Model):
    user = models.ForeignKey(UserReg, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
class SellerVehicle(models.Model):
    Approval = 'A'
    Not_approval = 'N'
    CHOICES=(
        ('Approval', 'Approval'),
        ('Not approval', 'Not approval'),
    )
    brandname=models.CharField(max_length=250,null=True)
    model = models.CharField(max_length=250,blank=True,null=True)
    sprice = models.DecimalField(max_digits=10, decimal_places=2)
    elocation = models.CharField(max_length=250,null=True)
    semail = models.CharField(max_length=250,null=True)
    sphonenumber = models.CharField(max_length=225,null=True)
    vimages=models.ImageField(upload_to='vehicle/uploads',default=None,blank=True)
    approvals = models.CharField(max_length=300, choices=CHOICES, default=Not_approval,null=True)
    def __str__(self):
        return self.brandname
    
    

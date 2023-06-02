from django.contrib import admin
from .models import UserReg
from .models import Vehicle
from .models import Order
from .models import Favourites
from .models import Addtocart
from .models import Wishlist
from .models import SellerVehicle,VehicleDetails

# Register your models here.
class UserRegAdmin(admin.ModelAdmin):
    list_display = ['id','username','password1','password2']
    search_fields = ['location','email']

admin.site.register(UserReg,UserRegAdmin)

class VehicleAdmin(admin.ModelAdmin):
    list_display=['id','image']

admin.site.register(Vehicle,VehicleAdmin)
    


class OrderAdmin(admin.ModelAdmin):
    list_display=['vehicleid']

admin.site.register(Order,OrderAdmin)
    
class FavouritesAdmin(admin.ModelAdmin):
    list_display=['vehicleid']

admin.site.register(Favourites,FavouritesAdmin)
    
class AddtocartAdmin(admin.ModelAdmin):
    list_display=['vehicleid']

admin.site.register(Addtocart,AddtocartAdmin)


class WishlistAdmin(admin.ModelAdmin):
    list_display=['user']

admin.site.register(Wishlist,WishlistAdmin)

class SellerVehicleAdmin(admin.ModelAdmin):
    list_display=['brandname']

admin.site.register(SellerVehicle,SellerVehicleAdmin)

class VehicleDetailAdmin(admin.ModelAdmin):
    list_display=['vuserid','vvehicleid']

admin.site.register(VehicleDetails,VehicleDetailAdmin)





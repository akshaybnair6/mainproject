import contextlib
from pyexpat.errors import messages
import time
from django.shortcuts import render,redirect
from .models import UserReg
from .models import Vehicle
from .models import SellerVehicle
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Wishlist
import cv2
import imutils
# import necessary machine learning libraries for object detection
from .models import Favourites, Vehicle, UserReg, VehicleDetails



#from django.contrib import messages
#from models import product
def home(request):
    display=UserReg.objects.all()
    dict={
        'data':display,
    }
    return render(request,'index.html',context=dict)
    return render(request,'index.html')

# ===========================================================================================
# registration
# ==================

def register(request):
     return render(request,'register.html')




# ===========================================================================================
# login
# ==================


def login(request):
    return render(request, 'login.html')


# ===========================================================================================

# logout
# =========================
def logout_view(request):
    logout(request)
    return redirect('home')

# =============================================================================================

# index | login view
# ==========================
def index_login_view(request):
    return render(request,'index.html')
def userchk(request):
    dict={
        'data':''
    }

    data=UserReg.objects.filter(username=request.POST.get('username'), password1=request.POST.get('password')).count()
    print(data)
    if(data>0):
        datas=UserReg.objects.filter(username=request.POST.get('username'), password1=request.POST.get('password'))
        request.session["id"]=datas[0].id
        dict = {
            'data': request.POST.get('username').upper()+' Logged in Successfully '
        }
        return render(request, 'UserDetails.html', context=dict)
    else:
        dict = {
            'data': 'Wrong Username Password'
        }
        return render(request, 'login.html', context=dict)
    return render(request,'login.html',context=dict)
def about(request):
    return render(request,'about.html')
def delete(request):
    i=request.GET["id"]
    display=UserReg.objects.get(id=i)
    display.delete()
    display=UserReg.objects.all()
    print(display)
    dict={
        'data':display,
    }
    return render(request,'userdisplay.html',context=dict)
def userdisplay(request):
    return render(request, 'userdisplay.html')
def userdisplay(request):
    display=UserReg.objects.filter(id=1)
    dict={
        'data':display,
    }
    return render(request,'userdisplay.html',context=dict)
def vehicledisplay(request):
    return render(request, 'vehicledisplay.html')
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'productcard.html', context)
def savedata(request):
    display=UserReg()
    display.username=request.POST.get('uname')
    display.password1=request.POST.get('pass')
    display.password2=request.POST.get('passw')
    display.email=request.POST.get('email')
    display.location=request.POST.get('location')
    display.phonenumber=request.POST.get('phnumber')

    display.save()
    return render(request,'login.html')
'''def add_product(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		price = request.POST.get('price')
		description = request.POST.get('description')

		if not name or not price or not description:
			messages.error(request, 'Please fill in all fields')
			return redirect('add_product')

		product = Product(name=name, price=price, description=description)
		product.save()

		messages.success(request, 'Product added successfully')
		return redirect('product_list')

	return render(request, 'addproduct.html')'''
def checkout(request):
    return render(request,'checkout.html')
def productcard(request):
    return render(request,'productcard.html')
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    context = {
        'vehicles': vehicles,
        }
    return render(request, 'productcard.html', context=context)
def base(request):
    return render(request,'base.html')
def userpage1(request):
    return render(request, 'userpage1.html')
def user_profile(request):
    # user = get_object_or_404(UserReg, username=request.user.username)
    # context = {'user': user}
    return render(request, 'user_profile.html',{})
# def product_wishlist(request):
#     # Retrieve the current user's wishlist items from the database
#     wishlist_items = Wishlist.objects.filter(user=request.user)

#     if request.method == 'POST':
#         # If the user submits a form to remove an item from their wishlist,
#         # retrieve the item from the database and delete it
#         item_id = request.POST.get('item_id')
#         item = Wishlist.objects.get(id=item_id)
#         item.delete()
#         return redirect('product_wishlist')

#     # Render the wishlist template with the retrieved wishlist items
#     return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


def vehicle_detail(request):
    vehicle = Vehicle.objects.filter(id=request.GET["id"])
    context = {'vehicles': vehicle}
    return render(request, 'vehicle_detail.html', context=context)

def buy_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=request.session["id"])

    if request.method == 'POST':
        # process the form submission
        # for example, you might create an order object
        # and associate it with the vehicle object
        # then redirect the user to a thank you page

        return redirect('thank_you')

    return render(request, 'buy_vehicle.html', {'vehicle': vehicle})

def add_to_wishlist(request):
    

# Get the vehicle and user objects
       # replace 2 with the actual user ID

# Create a new Favourites object and set its fields
    favourites = Favourites()
    favourites.vehicleid =get_object_or_404(Vehicle, pk=request.POST.get('vehicleid'))# replace 1 with the actual vehicle ID
    favourites.userid =get_object_or_404(UserReg, pk=request.session["id"])
    favourites.save()
    display={
        'data':favourites,
    }
    return render(request,"wishlist.html",context=display)

def wishlist_view(request):
    vehicleid=request.GET["vehicleid"]
    #userid=request.GET["userid"]
    #id=request.GET["id"]
    dict={
        'vehicleid':vehicleid,
        #'userid':userid,
        
    }
    return render(request,"wishlist.html",context=dict)

def favourite(request):
    display=Vehicle.objects.all()
    print(display)
    dict={
        'data':display,
    }
    return render(request,'wishlist.html',context=dict)

def vehicledetailsave(request):
    display=VehicleDetails()
    display.vvehicleid=get_object_or_404(Vehicle, pk=request.POST.get('vehicleid'))
    display.vuserid=get_object_or_404(UserReg, pk=request.session["id"])
    display.save()
    return vehicle_list(request)
    
def demo_update(request):
     return render(request,"user_profile.html",{})

def demo_update_view(request):
    display=UserReg.objects.get(id=request.session["id"])
    print(display)
    display.username=request.POST.get('name')
    display.password1=request.POST.get('password')
    display.password2=request.POST.get('cpassword')
    display.email=request.POST.get('email')
    display.location=request.POST.get('location')
    display.phonenumber=request.POST.get('phone')
    display.save()
    return render(request,"index.html",{})

def wishlist_demo_page(request):
   display=Vehicle.objects.filter(id=request.session["id"])
   print(display)
   dict={
         'data':display,
     }
   return render(request,"wishlist.html",context=dict)
def seller(request):
     return render(request,"seller.html",{})
def sellersad(request):
    display=SellerVehicle()
    display.brandname=request.POST.get('brand')
    display.model=request.POST.get('model')
    display.sprice=request.POST.get('price')
    display.semail=request.POST.get('email')
    display.elocation=request.POST.get('location')
    display.sphonenumber=request.POST.get('phone')
    display.vimages=request.POST.get('images')
    display.save()
    return approval(request)
def approval(request):
    display=SellerVehicle.objects.all()
    dict={
         'data':display,
     }
    return render(request,"approval.html",context=dict)
    
# def object_detection(request):
#     # initialize the video stream and wait for the camera to warm up
#     vs = cv2.VideoCapture(0)
#     time.sleep(2.0)

#     # loop over the frames from the video stream
#     while True:
#         # grab the frame from the video stream
#         ret, frame = vs.read()

#         # resize the frame and convert it to grayscale
#         frame = imutils.resize(frame, width=400)
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # perform object detection on the frame
#         # use your machine learning model to detect objects in the frame

#         # show the frame with detected objects
#         cv2.imshow("Frame", frame)

#         # check if the user has pressed the 'q' key to quit
#         key = cv2.waitKey(1) & 0xFF
#         if key == ord("q"):
#             break

#     # release the video stream and close all windows
#     vs.release()
#     cv2.destroyAllWindows()

#     # return the processed frames to the search bar
#     # convert the processed frames to a format that can be displayed in a web browser

# import cv2
# import numpy as np
# from django.http import HttpResponse
# from django.views.decorators import gzip

# # Load the pre-trained model for object detection
# net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# # Define the classes for the objects that can be detected
# classes = []
# with open("coco.names", "r") as f:
#     classes = [line.strip() for line in f.readlines()]

# # Set the minimum confidence threshold for object detection
# conf_threshold = 0.5

# # Define a function to perform object detection on each frame
# def detect_objects(frame):
#     # Get the dimensions of the frame
#     height, width, channels = frame.shape

#     # Create a blob from the frame and pass it through the network
#     blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), (0, 0, 0), True, crop=False)
#     net.setInput(blob)
#     outputs = net.forward(net.getUnconnectedOutLayersNames())

#     # Create lists to store the detected objects and their confidence levels
#     objects = []
#     confidences = []

#     # Loop through each output layer and detect objects in the frame
#     for output in outputs:
#         for detection in output:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]

#             if confidence > conf_threshold:
#                 # Get the center, width, and height of the bounding box
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)
#                 bbox_width = int(detection[2] * width)
#                 bbox_height = int(detection[3] * height)

#                 # Calculate the top-left corner of the bounding box
#                 top_left_x = int(center_x - (bbox_width / 2))
#                 top_left_y = int(center_y - (bbox_height / 2))

#                 # Add the detected object and its confidence level to the lists
#                 objects.append(classes[class_id])
#                 confidences.append(float(confidence))

#                 # Draw the bounding box and label for the detected object
#                 cv2.rectangle(frame, (top_left_x, top_left_y), (top_left_x + bbox_width, top_left_y + bbox_height), (0, 255, 0), 2)
#                 cv2.putText(frame, classes[class_id] + " " + str(round(confidence, 2)), (top_left_x, top_left_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     return frame

# # Define a Django view that captures the video stream from the laptop camera and performs object detection on each frame
# @gzip.gzip_page
# def video_feed(request):
#     # Open the laptop camera
#     cap = cv2.VideoCapture(0)

#     while True:
#         # Read a frame from the camera
#         ret, frame = cap.read()

#         if not ret:
#             break

#         # Perform object detection on the frame
#         processed_frame = detect_objects(frame)

#         # Convert the processed frame to JPEG format and return it as an HTTP response
#         ret, buffer = cv2.imencode('.jpg', processed_frame)
#         response = HttpResponse(buffer.tobytes(), content_type='image/jpeg')
#         yield response.write(contextlib)

#     cap.release()
# def wishlist(request):
#     wishlist = get_object_or_404(Wishlist, userid=request.userid)
#     products = wishlist.products.all()
#     customer = UserReg.objects.get(id=request.id)
#     context = {
#         'customer': customer,
#         'products': products,
#     }
#     if not products:
#         context['empty_wishlist'] = True
#     return render(request, 'wishlist.html', context)


# def add_to_wishlist(request, product_id):
#     product = get_object_or_404(Vehicle, id=id)
#     wishlist, created = Wishlist.objects.get_or_create(user=request.user)
#     wishlist.products.add(product)
#     messages.success(request, f"{product.prd_name} has been added to your wishlist.")
#     return redirect('wishlist')
def lastpage(request):
     return render(request,'thanks.html')
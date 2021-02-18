from django.shortcuts import render
from django.http import HttpResponse
from Movieapp.forms import Movieform,CustomerForm,showsForm,Bookingform
from Movieapp.models import Movie,Customer,Admin,Shows,Bookings
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,'Movieapp/index.html')

def addmovie(request):
    if request.method=="POST":
        movieform = Movieform(request.POST,request.FILES)
        if movieform.is_valid():
            movieform.save()
            return render(request,'Movieapp/addmovie.html',{"status":"Movie is Added"})
        else:
            return render(request,'Movieapp/addmovie.html',{"status":"Movie is Not Added"})
    else:
        return render(request,'Movieapp/addmovie.html')

#show movielist from the Database:
def Movielist(request):
    movielist = Movie.objects.all()
    return render(request,'Movieapp/movielist.html',{"movielist":movielist})

def deletemovie(request,MovieId):
    movie=Movie.objects.get(MovieId=MovieId)  #get method returns movie by attribute

    movie.delete()
    movielist = Movie.objects.all()
    return render(request,'Movieapp/movielist.html',{"status":"movie Deleted Successfully","movielist":movielist})


#update Movie
def updatemovie(request,MovieId):
    print(request.method,'hii')
    if request.method=="GET":
        movie = Movie.objects.get(MovieId=MovieId)    #get method returns movie by attribute
        return render(request,"Movieapp/updatemovie.html",{'updatemovie':movie})      
    elif request.method == "POST":
        movie = Movie.objects.get(MovieId=MovieId)
        movieform = Movieform(request.POST,request.FILES,instance=movie)
#here instance telling to server that form having the details of instance
        if movieform.is_valid():
            movieform.save() #because of instasnce property new object will not create here
            movielist=Movie.objects.all()  #fetch All the updated movies
            return render(request,"Movieapp/movielist.html",{'status':'Movie Updated','movielist':movielist})
        else:
            return render(request,'Movieapp/updatemovie.html',{'status':'Movie Not Updated','updatemovie':Movie})


def addcustomer(request):
    if request.method=="POST":
        customerform = CustomerForm(request.POST,request.FILES)
        if customerform.is_valid():
            customerform.save()
            return render(request,'Movieapp/addcustomer.html',{"status":"Information is Added"})
        else:
            return render(request,'Movieapp/addcustomer.html',{"status":"Information is Not Added"})
    else:
        return render(request,'Movieapp/addcustomer.html')

def Customerlist(request):
    customerlist = Customer.objects.all()
    return render(request,'Movieapp/customerlist.html',{"customerlist": customerlist})


def login(request):
    if request.method == 'GET':
        #show the login form
        return render(request,'Movieapp/login.html')
    elif request.method == 'POST':
        #here we fetch login details from login form fill by customer or admin
        
        usertype = request.POST['usertype']
        username = request.POST['username']
        password = request.POST['password']
        if usertype == 'Admin': 
            try:
                admin = Admin.objects.get(adminEmailId=username,adminPassword=password)
                if admin.adminEmailId == username and admin.adminPassword == password:
                    request.session['admin']=admin.adminEmailId
                    return render(request,'Movieapp/index.html',{'status':'Admin login Successfully'})
                else:
                    return render(request,'Movieapp/login.html',{'status':'Admin login UnSuccessfully'})
            except Exception as e: 
                return render(request,'Movieapp/login.html',{'status':'Admin login UnSuccessfully.','error':e})


        elif usertype == 'Customer':
            try:
                customer = Customer.objects.get(custEmail=username,custPassword=password)
                if customer.custEmail == username and customer.custPassword == password:
                    request.session["customer"]=customer.custEmail
                    request.session["customerDetails"]={"custName":customer.custName,"custLname":customer.custLname}

                    return render(request,'Movieapp/index.html',{'status':'Customer login Successfully'})
                else:
                    return render(request,'Movieapp/login.html',{'status':'Customer login UnSuccessfully'})
            except Exception as e: 
                    return render(request,'Movieapp/login.html',{'status':'Customer login UnSuccessfully.','error':e})
def logout(request):
    session_key = list(request.session.keys())
    #here we deleting our session
    for key in session_key:
        del request.session[key] 
    return render(request,'Movieapp/index.html',{'status':'Logout Successfully.'})



def addshows(request):
    if request.method == "GET":
        movielist = Movie.objects.all()
        return render(request,'Movieapp/addshows.html',{'movielist':movielist})
    elif request.method == 'POST':
        showform = showsForm(request.POST)
        print(showform)
        if showform.is_valid():
            showform.save()
            return render(request,'Movieapp/addshows.html',{"movielist": Movielist,"status":'Show is Created Successfully'})
        else:
            return render(request,'Movieapp/addshows.html',{"movielist": Movielist,"status":'Show is Not Created'})


def showlist(request):
    showlist = Shows.objects.all()
    return render(request,'Movieapp/showlist.html',{"showlist": showlist})

def UpdateShows(request,showId):
    if request.method == 'GET':
        movielist = Movie.objects.all()
        show = Shows.objects.get(showId=showId)
        return render(request,'Movieapp/UpdateShows.html',{"movielist":movielist,'show':show})
    elif request.method == "POST":

        show = Shows.objects.get(showId=showId)
        showformobj = showsForm(request.POST,request.FILES,instance=show)
#here instance telling to server that form having the details of instance
        if showformobj.is_valid():
            showformobj.save() #because of instasnce property new object will not create here
            showlist=Shows.objects.all() #fetch All the updated movies
            return render(request,"Movieapp/UpdateShows.html",{'status':'show Updated','showlist':showlist})
        else:
            return render(request,'Movieapp/UpdateShows.html',{'status':'Show Not Updated','showlist':Shows})

def deleteshows(request,showId):
    try:
        show=Shows.objects.get(showId=showId)  #get method returns movie by attribute

        show.delete()
        showlist = Shows.objects.all()
        return render(request,'Movieapp/showlist.html',{"status":"show Deleted Successfully","showlist":showlist})
    except Exception as e:
        return render(request,'Movieapp/showlist.html',{"status":"show Deleted Successfully","showlist":Shows})
        

def bookshowSeats(request,showId):
    if request.method=="GET":
        show = Shows.objects.get(showId=showId)
        cols= ['1','2','3','4','5',' ','6','7','8','9','10','11','12']
        
        return render(request,'Movieapp/selectseats.html',{"show":show,'cols':cols})



def bookTheShow(request):
    if request.method =='POST':
        sId= request.POST['bookedShow'] #here we are getting showId from request
        bshow = Shows.objects.get(showId = sId)  #using that should of that id and save in booking
        #from will do this automatic for you
        bseats=request.POST['bookedSeats']
        tprice=request.POST['totalPrice']
        cEmail = request.session['customer']
        bDate = datetime.now()   #here we create a manual object of booking model with above details
        bookedshow = Bookings.objects.create(bookedshow= bshow,bookedSeats=bseats,totalPrice= tprice,custEmail=cEmail,bookingDate=bDate,bookingStatus ='Booked')  #again we get This booked show is( Current booked show) form database with BookingId
        bookedshow.save()
        # again we get this booked show i.e  (current bookedshow) from database with Bookingid
        bookedshow = Bookings.objects.get(custEmail=cEmail,bookingDate=bDate)


        return render (request,'Movieapp/bookingDetails.html',{'status':'Show is booked ','bookedshow':bookedshow})


        
          
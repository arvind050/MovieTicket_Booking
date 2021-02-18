from django.db import models

# Create your models here.
class Movie(models.Model):
    MovieId = models.AutoField(primary_key=True)
    MovieName = models.CharField(max_length=50)
    MovieType = models.CharField(max_length=50)
    MovieLanguage = models.CharField(max_length=50)
    MovieCast = models.CharField(max_length=50)
    MovieDuratiuon = models.CharField(max_length=50)
    ReleaseDate  = models.CharField(max_length=50)
    MovieImage = models.ImageField(upload_to="MovieImage/",default="No-image.jpg")
    class Meta:
        db_table= 'movie_005' 


class Customer(models.Model):
    custId = models.AutoField(primary_key=True)
    custName = models.CharField(max_length=50)
    custLname = models.CharField(max_length=50)
    custEmail = models.CharField(max_length=50,unique=True)
    custPassword = models.CharField(max_length=50)
    custContact = models.CharField(max_length=12)
    custAddress = models.CharField(max_length=225)
    class Meta:
        db_table= 'customer_005'

class Admin(models.Model):
    adminEmailId = models.CharField(primary_key=True,max_length=30)
    adminPassword = models.CharField(max_length=30)
    class Meta:
        db_table = 'admin_308'

class Shows(models.Model):
    showId = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    # when movie get delete show also deleted  Automatically
    theater = models.CharField(max_length=100)
    screen = models.CharField(max_length=20)
    showDate = models.CharField(max_length=50)
    showTime = models.CharField(max_length=50)
    showPrice = models.FloatField(max_length=50)
    class Meta:
        db_table = 'shows_308'
        
class Bookings(models.Model):
    bookingId = models.AutoField(primary_key=True)
    bookedshow = models.ForeignKey(Shows,on_delete=models.CASCADE)  #here we going store showId
    bookedSeats = models.CharField(max_length=101)
    totalPrice = models.FloatField(max_length=50)
    bookingDate = models.CharField(max_length=50)
    bookingStatus = models.CharField(max_length=50,default='Processing')
    custEmail= models.CharField(max_length=70,default='Annoymus')
    class Meta:
        db_table = 'booking_308'

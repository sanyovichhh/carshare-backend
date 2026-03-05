from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.PositiveIntegerField() 
    number_plate = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=30)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    user_phone = models.CharField(max_length=20)
    status = models.CharField(max_length=10)

class Booking(models.Model):
    # User 1 -> Booking (Один пользователь — много бронирований)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    
    # Car 1 -> Booking (Одна машина — много бронирований)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    book_status = models.CharField(max_length=30)

class Trip(models.Model):
    # Booking 1 -> 1 Trip (Одно бронирование — одна поездка)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, primary_key=True)
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
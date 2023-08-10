from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu,Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        
class MenuSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Menu
        fields = ('ID', 'Title', 'price', 'Inventory')
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('ID', 'name', 'No_of_guests', 'Booking_date')
        
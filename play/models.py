from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_CHOICES = [
        ('B', 'as bronze'),
        ('S', 'as silver'),
        ('G', 'as gold'),
    ]
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    brith_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='B')
    player = models.ForeignKey(Player,on_delete=models.CASCADE)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)








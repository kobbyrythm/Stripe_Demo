from django.db import models


class Event(models.Model):
    id = models.BigAutoField( primary_key=True)
    name = models.CharField(max_length=70,verbose_name='Event Name')
    description = models.TextField(max_length=800,verbose_name='Description')
    price = models.FloatField(verbose_name='Price')
    seller_id = models.ForeignKey('payment.Seller',on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name
    

class Payments(models.Model):
    payment_id = models.AutoField
    seller_id = models.ForeignKey('payment.Seller', on_delete=models.CASCADE)
    buyer_id = models.ForeignKey('payment.Buyer', on_delete=models.CASCADE)
    transaction_fee = models.DecimalField(max_digits=4,decimal_places=2)
    commission = models.FloatField(default=0.0)

    def __str__(self):
        return self.payment_id


class Buyer(models.Model):
    buyer_id = models.AutoField
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Seller(models.Model):
    seller_id = models.AutoField
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

class Company(models.Model):
    company_id = models.AutoField
    name = models.CharField(max_length=200)




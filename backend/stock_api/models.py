from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class StockCompany(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

class RecommendedStock(models.Model):
    class MarketType(models.TextChoices):
        KOSPI = "KOSPI", "KOSPI 종합"
        KOSDAQ = "KOSDAQ", "KOSDAQ 종합"

    stock_company = models.ForeignKey(StockCompany,on_delete=models.SET_NULL, blank=True,null=True)
    stock_item_name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)
    market = models.CharField(max_length=10, choices=MarketType.choices, blank=True, null=True)
    recommended_date = models.DateField(blank=True, null=True)
    recommended_price = models.IntegerField(blank=True, null=True)
    prev_close = models.IntegerField(blank=True, null=True)
    dividend_rate = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    

    

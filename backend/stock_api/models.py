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

class StockReport(models.Model):

    pdf_name = models.CharField(max_length=300, blank=True, null=True) 
    wdate = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=300, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    stock_broker = models.ForeignKey(StockCompany,on_delete=models.SET_NULL, blank=True,null=True)
    target_opinion = models.CharField(max_length=300, blank=True, null=True)
    target_price = models.IntegerField(blank=True, null=True)
    report_link = models.CharField(max_length=300, blank=True, null=True)
    pdf_text = models.TextField(blank=True, null=True)
    pdf_summerize = models.TextField(blank=True, null=True)
    pdf_sent_score = models.DecimalField(max_digits=30, decimal_places=5, blank=True, null=True)
    pdf_sent_topic = models.CharField(max_length=300, blank=True, null=True)

class Kospi(models.Model):

    Code = models.CharField(max_length=30, blank=True, null=True)
    Name = models.CharField(max_length=30, blank=True, null=True)
    Current= models.IntegerField(blank=True, null=True)
    Mkt = models.CharField(max_length=30, blank=True, null=True)
    Status = models.CharField(max_length=30, blank=True, null=True)
    PER = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    PBR = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    EPS = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    BPS = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)


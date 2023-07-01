from django.contrib import admin
from .models import Animal
from .models import RecommendedStock, StockCompany
from .models import StockReport, StockCompany
from .models import Kospi


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner')  # 리스트 뷰 필드 추가

class StockCompanyAdmin(admin.ModelAdmin):
    list_display = ['name']

class RecommendedStockAdmin(admin.ModelAdmin):
        list_display = (
            "stock_company", "stock_item_name",
            "code", 
            "market", 
            "recommended_date", "recommended_price", "prev_close", 
            "dividend_rate", 
            "reference")

class StockReportAdmin(admin.ModelAdmin):
    list_display = (
            "pdf_name", 
            "wdate", 
            "company",
            "title",
            "content",
            "stock_broker",
            "target_opinion",
            "target_price",
            "report_link",
            "pdf_text",
            "pdf_summerize",
            "pdf_sent_score",
            "pdf_sent_topic")

class KospiAdmin(admin.ModelAdmin):
    list_display = (
            "Code",
            "Name",
            "Current",
            "Mkt",
            "Status",
            "PER",
            "PBR",
            "EPS",
            "BPS")

admin.site.register(Animal, AnimalAdmin)
admin.site.register(StockCompany, StockCompanyAdmin)
admin.site.register(RecommendedStock, RecommendedStockAdmin)
admin.site.register(StockReport, StockReportAdmin)
admin.site.register(Kospi, KospiAdmin)

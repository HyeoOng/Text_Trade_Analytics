from django.contrib import admin
from .models import Animal
from .models import RecommendedStock, StockCompany

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

admin.site.register(Animal, AnimalAdmin)
admin.site.register(StockCompany, StockCompanyAdmin)
admin.site.register(RecommendedStock, RecommendedStockAdmin)

from rest_framework import serializers
from .models import Animal
from .models import StockCompany
from .models import RecommendedStock

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ["name", "owner", "type"]

class StockCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockCompany
        fields = ["name"]
        
class RecommendedStockSerializer(serializers.ModelSerializer):
    stock_company = StockCompanySerializer()

    class Meta:
        model = RecommendedStock
        fields = ["stock_company",
        "stock_item_name",
        "code",
        "market",
        "recommended_date",
        "recommended_price",
        "prev_close",
        "dividend_rate",
        "reference"]
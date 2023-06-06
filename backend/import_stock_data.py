import os
import csv
import pandas as pd
import django
from django.db import transaction
from datetime import datetime


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from stock_api.models import RecommendedStock, StockCompany

FILE_NAME = 'recommended_stocks_origin.csv'  


@transaction.atomic
def import_data():
    csv_file = FILE_NAME

    # Read the CSV file using pandas
    data = pd.read_csv(csv_file)

    for _, row in data.iterrows():
        stock_company_name = row['stock_company']
        stock_item_name = row['stock_item']
        market = RecommendedStock.MarketType.KOSPI if row['market'] == "KOSPI 종합" else RecommendedStock.MarketType.KOSDAQ

        # code
        code = int(row['code'])
        code = str(abs(code))
        code = code.zfill(6)
        
        # recommended_date
        recommended_date_str = row['recommended_date']
        recommended_date = datetime.strptime(recommended_date_str, "%Y.%m.%d").date()
        
        # recommended_price
        recommended_price_str = row['recommended_price']
        recommended_price = int(recommended_price_str.replace(",", ""))

        # prev_close
        prev_close_str = row['prev_close']
        prev_close = int(prev_close_str.replace(",", ""))

        # dividend_rate
        dividend_rate_str = row['devidend_rate']        
        dividend_rate = float(dividend_rate_str.strip("%"))

        reference = row['reference']

        # StockCompany 만들기
        stock_company, _ = StockCompany.objects.get_or_create(name=stock_company_name)

        # RecommendedStock 만들기
        recommended_stock = RecommendedStock(
            stock_company=stock_company,
            stock_item_name=stock_item_name,
            code=code,
            market=market,
            recommended_date=recommended_date,
            recommended_price=recommended_price,
            prev_close=prev_close,
            dividend_rate=dividend_rate,
            reference=reference
        )
        recommended_stock.save()

    print("데이터 복사 완료~!")

if __name__ == '__main__':
    import_data()

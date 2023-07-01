import os
import csv
import pandas as pd
import django
from django.db import transaction
from datetime import datetime


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from stock_api.models import StockReport, StockCompany

FILE_NAME = 'pdf_text_last.csv'


@transaction.atomic
def import_data():
    csv_file = FILE_NAME

    # Read the CSV file using pandas
    data = pd.read_csv(csv_file)

    for _, row in data.iterrows():
# row 를 한국어로 바꾸기
        stock_broker = row['증권사']
        stock_broker, _ = StockCompany.objects.get_or_create(name=stock_broker)

        company = row['종목명']
        
        # pdf_name
        pdf_name = row['pdf이름']

        # wdate
        wdate_str = row['날짜']
        wdate = datetime.strptime(wdate_str, "%Y.%m.%d").date()

        # title
        title = row['제목']
        
        #content
        content = row['내용']
        
        # target_opinion
        target_opinion = row['의견']

        # target_price
        target_price = None if row['목표가'] == "-9999" else int(row['목표가'])

        # report_link
        report_link_str = row['리포트링크']

        # pdf_text
        pdf_text = row['텍스트']

        # pdf_summerize
        pdf_summerize = row['요약문']

        # pdf_sent_score
        pdf_sent_score = float(row['감성점수'])

        # pdf_sent_topic
        pdf_sent_topic = row['감성토픽']

        # StockReport 만들기
        stockreport = StockReport(
            stock_broker = stock_broker,
            company = company,
            pdf_name  = pdf_name,
            wdate = wdate,
            title = title,
            content = content,
            target_opinion = target_opinion,
            target_price = target_price,
            report_link = report_link_str,
            pdf_text = pdf_text,
            pdf_summerize  = pdf_summerize,
            pdf_sent_score = pdf_sent_score,
            pdf_sent_topic = pdf_sent_topic,
        )
        stockreport.save()

    print("데이터 복사 완료~!")

if __name__ == '__main__':
    import_data()

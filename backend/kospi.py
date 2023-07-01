import os
import json
import django
from django.db import transaction
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from stock_api.models import Kospi

FILE_NAME = 'kospi.json'


@transaction.atomic
def import_data():
    json_file = FILE_NAME

    # Read the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    for _, row in data.items():
        Code = row['Code']
        Name = row['Name']
        Current = row['Current']
        Mkt = row['Mkt']
        Status = row['Status']
        PER = row['PER']
        PBR = row['PBR']
        EPS = row['EPS']
        BPS = row['BPS']

        kospi = Kospi(
            Code=Code,
            Name=Name,
            Current=Current,
            Mkt=Mkt,
            Status=Status,
            PER=PER,
            PBR=PBR,
            EPS=EPS,
            BPS=BPS
        )
        kospi.save()

    print("데이터 복사 완료~!")


if __name__ == '__main__':
    import_data()

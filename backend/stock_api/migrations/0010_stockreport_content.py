# Generated by Django 4.2.1 on 2023-06-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_api', '0009_alter_stockreport_company_alter_stockreport_pdf_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockreport',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
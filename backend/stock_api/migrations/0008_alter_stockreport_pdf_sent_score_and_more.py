# Generated by Django 4.2.1 on 2023-06-12 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_api', '0007_alter_stockreport_pdf_name_delete_pdfname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockreport',
            name='pdf_sent_score',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='stockreport',
            name='stock_broker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_api.stockcompany'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-12 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_api', '0008_alter_stockreport_pdf_sent_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockreport',
            name='company',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='stockreport',
            name='pdf_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='stockreport',
            name='pdf_sent_topic',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='stockreport',
            name='report_link',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='stockreport',
            name='target_opinion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='stockreport',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_api', '0010_stockreport_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kospi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(blank=True, max_length=30, null=True)),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Current', models.IntegerField(blank=True, null=True)),
                ('Mkt', models.CharField(blank=True, max_length=30, null=True)),
                ('Status', models.CharField(blank=True, max_length=30, null=True)),
                ('PER', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('PBR', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('EPS', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('BPS', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stockreport',
            name='pdf_sent_score',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=30, null=True),
        ),
    ]
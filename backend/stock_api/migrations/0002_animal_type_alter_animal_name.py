# Generated by Django 4.2.1 on 2023-06-06 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="type",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="animal",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

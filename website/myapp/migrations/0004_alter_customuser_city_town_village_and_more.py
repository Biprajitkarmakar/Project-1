# Generated by Django 4.2 on 2025-03-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_customuser_city_town_village_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city_town_village',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City/Town/Village'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='pin_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='street_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

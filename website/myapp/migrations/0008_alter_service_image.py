# Generated by Django 4.2 on 2025-03-31 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='service_images/'),
        ),
    ]

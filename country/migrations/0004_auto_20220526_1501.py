# Generated by Django 3.2.9 on 2022-05-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20220526_1501'),
        ('country', '0003_contentcountry_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='country_info',
        ),
        migrations.AlterField(
            model_name='country',
            name='country_images',
            field=models.ManyToManyField(db_table='country_images', to='gallery.Image'),
        ),
    ]

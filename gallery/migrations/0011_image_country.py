# Generated by Django 3.2.9 on 2022-05-28 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0006_auto_20220528_1635'),
        ('gallery', '0010_auto_20220527_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='country',
            field=models.ManyToManyField(db_table='country_images', to='country.Country'),
        ),
    ]
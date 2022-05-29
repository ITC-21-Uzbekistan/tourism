# Generated by Django 3.2.9 on 2022-05-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20220526_1501'),
        ('tour', '0003_contenttour_contenttypetour_tour_typetour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='tour_info',
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_images',
            field=models.ManyToManyField(db_table='tour_images', to='gallery.Image'),
        ),
    ]

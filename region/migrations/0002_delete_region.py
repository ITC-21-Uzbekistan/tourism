# Generated by Django 3.2.9 on 2022-05-22 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20220522_2332'),
        ('shrine', '0002_delete_shrine'),
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Region',
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-28 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0005_auto_20220527_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='region',
            name='deleted_by',
        ),
    ]
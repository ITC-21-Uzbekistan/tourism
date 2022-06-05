# Generated by Django 3.2.9 on 2022-05-31 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='alt_text',
        ),
        migrations.RemoveField(
            model_name='image',
            name='country',
        ),
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
        migrations.RemoveField(
            model_name='image',
            name='region',
        ),
        migrations.RemoveField(
            model_name='image',
            name='shrine',
        ),
        migrations.RemoveField(
            model_name='image',
            name='tour',
        ),
        migrations.AddField(
            model_name='image',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-31 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20220601_0001'),
        ('shrine', '0004_auto_20220601_0001'),
        ('tour', '0003_contenttour_contenttypetour_tour_typetour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='tour_info',
        ),
        migrations.AddField(
            model_name='tour',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_images',
            field=models.ManyToManyField(db_table='tour_images', to='gallery.Image'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_shrines',
            field=models.ManyToManyField(db_table='tour_shrines', to='shrine.Shrine'),
        ),
        migrations.CreateModel(
            name='TourShrine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_tour_id', models.IntegerField()),
                ('shrine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shrine.shrine')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour')),
            ],
            options={
                'db_table': 'tour_orders',
            },
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-22 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('relation', '0003_primarykeysofimages'),
        ('shrine', '0003_contentshrine_shrine'),
        ('language', '0001_initial'),
        ('tour', '0002_auto_20220522_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=255)),
                ('tour_info', models.TextField()),
                ('tour_price', models.FloatField(null=True)),
                ('tour_url', models.CharField(max_length=1000)),
                ('tour_images', models.ManyToManyField(to='relation.PrimaryKeysOfImages')),
                ('tour_shrines', models.ManyToManyField(to='shrine.Shrine')),
                ('tour_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour.typetour')),
            ],
        ),
        migrations.CreateModel(
            name='ContentTypeTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='language.language')),
                ('type_tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour.typetour')),
            ],
        ),
        migrations.CreateModel(
            name='ContentTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=255)),
                ('tour_info', models.TextField()),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='language.language')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour.tour')),
            ],
        ),
    ]
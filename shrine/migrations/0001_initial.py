# Generated by Django 3.2.9 on 2022-05-10 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
        ('relation', '0001_initial'),
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shrine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('url', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=1000)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.country')),
                ('images', models.ManyToManyField(to='relation.PrimaryKeysOfImages')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.region')),
            ],
        ),
    ]

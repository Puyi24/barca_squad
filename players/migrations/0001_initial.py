# Generated by Django 4.0.4 on 2022-05-29 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField()),
                ('profile_pic', models.ImageField(blank=True, default='', upload_to='')),
                ('birth_date', models.DateField()),
                ('nationality', models.CharField(max_length=60)),
                ('position', models.CharField(choices=[('GK', 'Goalkeeper'), ('LB', 'Left Back'), ('CB', 'Center Back'), ('RB', 'Right Back'), ('CDM', 'Central Defensive Midfielder'), ('CM', 'Central Midfielder'), ('CAM', 'Central Attacking Midfielder'), ('LW', 'Left Winger'), ('ST', 'Striker'), ('RW', 'Right Winger')], max_length=3)),
                ('shirt_num', models.CharField(max_length=2, unique=True)),
                ('debut', models.DateField()),
                ('trophies', models.TextField()),
            ],
        ),
    ]

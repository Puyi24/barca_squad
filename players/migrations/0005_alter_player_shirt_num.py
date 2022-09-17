# Generated by Django 4.0.4 on 2022-05-29 23:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_alter_player_shirt_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='shirt_num',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
    ]
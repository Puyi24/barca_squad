# Generated by Django 4.0.4 on 2022-06-10 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0019_alter_player_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default=''),
        ),
    ]

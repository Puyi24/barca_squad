# Generated by Django 4.0.4 on 2022-06-07 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('players', '0014_alter_player_bio_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='admin_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

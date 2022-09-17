from django.db import models
from django.contrib.auth.models import User
import django.core.validators as validators


class Player(models.Model):
    full_name = models.CharField(max_length=60)
    short_name = models.CharField(max_length=11)
    slug = models.SlugField()
    list_pic = models.ImageField(default="")
    details_pic = models.ImageField(default="")
    birth_date = models.DateField()
    nationality = models.CharField(max_length=60)
    position = models.CharField(max_length=3, choices=[
        ('GK', 'Goalkeeper'),
        ('LB', 'Left Back'),
        ('CB', 'Center Back'),
        ('RB', 'Right Back'),
        ('CDM', 'Central Defensive Midfielder'),
        ('CM', 'Central Midfielder'),
        ('CAM', 'Central Attacking Midfielder'),
        ('LW', 'Left Winger'),
        ('ST', 'Striker'),
        ('RW', 'Right Winger')
    ])
    shirt_num = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(99)],
                                    unique=True)
    facebook_link = models.URLField(max_length=100, default="", blank=True)
    instagram_link = models.URLField(max_length=100, default="", blank=True)
    twitter_link = models.URLField(max_length=100, default="", blank=True)
    bio_headline = models.CharField(max_length=200)
    player_bio = models.TextField()
    added_by = models.ForeignKey(User, default=None, limit_choices_to={'is_staff': True}, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.short_name


class Comment(models.Model):
    player = models.ForeignKey(Player, related_name="comments", on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.posted_by} on {str(self.player)}'

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now_add=True)


class League(models.Model):
    commissioner = models.ForeignKey(UserProfile, related_name="commissioner", on_delete=models.CASCADE) 
    name = models.CharField(max_length = 100)
    num_teams = models.IntegerField(default=10, validators=[
            MaxValueValidator(12),
            MinValueValidator(2),
        ])
    authenticated_users = models.ManyToManyField(UserProfile, related_name="team_members",)


class Team(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    icon = models.ImageField() # create default icon
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    wins_per = models.IntegerField() # percentage?
    trades = models.IntegerField(default=0)
    acquisitions = models.IntegerField(default=0)
    games_back = models.IntegerField(default=0)
    points_for = models.IntegerField(default=0)
    points_against = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    in_play = models.IntegerField()
    to_play = models.IntegerField()
    proj_points = models.IntegerField()

class Player(models.Model):
    POWER_FIVE = (
    ('Atlantic Coast Conference', 'ACC'),
    ('Big 12', 'Big%2012'),
    ('Big 10', 'Big%20Ten'),
    ('South Eastern Conference', 'SEC'),
    ('Pacific-12', 'Pac-12')
        )
    player_id = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True) # if null, show up on available player list
    is_available = models.BooleanField(default=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    conference = models.CharField(max_length=100, choices=POWER_FIVE)
    jersey_number = models.IntegerField()
    avg_points = models.IntegerField()
    health_status = models.CharField(max_length=100)

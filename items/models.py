
from django.db import models

# Create your models here.
class Item(models.Model):
    player_name = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    price = models.DecimalField
    description = models.TextField(max_length=350)
    condition = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.team_name} - {self.player_name}'
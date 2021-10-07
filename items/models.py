
from django.db import models

# Create your models here.
class Item(models.Model):
    player_name = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=350)
    condition = models.CharField(max_length=50)
    liked_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name = 'liked_items',
        blank = True
    )
    sold_by = models.ForeignKey(
        'jwt_auth.User',
        related_name = 'item_to_sell',
        on_delete = models.CASCADE
    )
    bought_by = models.ForeignKey(
        'jwt_auth.User',
        related_name = 'item_bought',
        null = True,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return f'{self.team_name} - {self.player_name}'

class Comment(models.Model):
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(
        Item,
        related_name = 'comments',
        on_delete = models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name = 'comments_made',
        on_delete = models.CASCADE
    )

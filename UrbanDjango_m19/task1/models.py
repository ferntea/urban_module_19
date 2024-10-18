from django.db import models

# Create your models here.
from django.db import models
# from task1.models import Buyer
class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Username of the buyer
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Balance
    age = models.PositiveIntegerField()  # Age of the buyer

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=255)  # Title of the game
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Cost of the game
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Size of the game files
    description = models.TextField()  # Description of the game
    age_limited = models.BooleanField(default=False)  # Age restriction
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Buyers who own the game

    def __str__(self):
        return self.title

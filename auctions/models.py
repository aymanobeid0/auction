from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils import timezone


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Auction (models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    starting_bid = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(
        blank=True, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXaRKTiE4Cu5dK-7WDq03H_7BN25TAak8U2fOLKbctt4ySr9tkt1ByA2LO3Nz-bTZ6_eI&usqp=CAU')
    date_created = models.DateTimeField(
        auto_now_add=True)
    isclosed = models.BooleanField(null=True, blank=True, default=False)
    iswatch = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.title


class Bid(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} bid {self.amount} $ on {self.auction}"


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.comment


# class Watch(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     auction_watched = models.ForeignKey(Auction, on_delete=models.CASCADE)

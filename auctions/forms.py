from django import forms
from django.forms.fields import DecimalField

from .models import *


class AuctionForm(forms.ModelForm):

    class Meta:
        model = Auction
        fields = ['title', 'description',
                  'category', 'starting_bid', 'image_url']


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        widgets = {'amount':
                   forms.TextInput(attrs={'class': 'form-control'})}

from django.forms import *

from .models import *


class AuctionForm(ModelForm):

    class Meta:
        model = Auction
        fields = ['title', 'description',
                  'category', 'starting_bid', 'image_url']


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        widgtes = {'amount': DecimalField(
            attrs={'class': 'form-control'})}

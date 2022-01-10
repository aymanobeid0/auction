Listing Page:
 
 
 1- Clicking on a listing should take users to a page specific to that listing.
   On that page, users should be able to view all details about the listing,
   including the current price for the listing.



2- If the user is signed in, the user should be able to add the item to their “Watchlist.” 
 If the item is already on the watchlist, the user should be able to remove it.



3- If the user is signed in, the user should be able to bid on the item.
   The bid must be at least as large as the starting bid, 
   and must be greater than any other bids that have been placed (if any). 
   If the bid doesn’t meet those criteria, the user should be presented with an error.
  
4- If the user is signed in and is the one who created the listing,
   the user should have the ability to “close” the auction from this page,
   which makes the highest bidder the winner of the auction and makes the listing no longer active.



5- If a user is signed in on a closed listing page, and the user has won that auction,
   the page should say so.
   Users who are signed in should be able to add comments to the listing page.
   The listing page should display all comments that have been made on the listing.




Watchlist:
   
1- Users who are signed in should be able to visit a Watchlist page, 
   which should display all of the listings that a user has added to their watchlist.


2- Clicking on any of those listings should take the user to that listing’s page.



Categories:

1- Users should be able to visit a page that displays a list of all listing categories.
   Clicking on the name of any category should take the user to a page that displays 
   all of the active listings in that category.
2- Django Admin Interface: Via the Django admin interface, a site administrator should be able to view,
   add, edit, and delete any listings, comments, and bids made on the site.
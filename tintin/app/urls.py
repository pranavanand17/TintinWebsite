# /mnt/c/Users/prana/TinTinMarket/tintin/app/urls.py

from django.urls import path
from .views import display_thumbnails,author,homepage

urlpatterns = [
    path('',homepage,name="homepage"),
    path('library/', display_thumbnails, name='library'),
    #path('bookoftheday/',book_of_the_day,name='bookoftheday'),
    path('author/',author,name='author'),
]

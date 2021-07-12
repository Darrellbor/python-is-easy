"""
    Title: variables.py
    Description: This file demonstrates my understanding of the 
    variables section of python is easy course
"""

# Module for date and time operations
import datetime


# title: The title of the song
title = 'Fling'
# artist: The artist of the song
artist = 'Jody'
# album: The album name
album = 'Waves Ep'
# album artist: The artist of the album
album_artist = 'Jody'
# genre: The genre of the album
genre = 'wordwide'
# year: The year the album was released
year = 2019
# total number of tracks: The total number of tracks the album has
total_number_of_tracks = 6
# rating: The current rating over 5 the album has
rating = 4
# is lyrics available: a boolean value indicating whether or not lyrics are available in the album
is_lyrics_available = True
# date released: The exact date the album was released
# Note: the date is equated to the current date
date_released = datetime.datetime.now()

# Print: Display all the attributes above
print(title, artist, album, album_artist, genre, year, total_number_of_tracks, rating, is_lyrics_available, date_released)

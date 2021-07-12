"""
    Title: dict.py
    Description: This file demonstrates my understanding of the 
    dictionary section of python is easy course
"""

# Module for date and time operations
import datetime

album_data = {
    # title: The title of the song
    "title": 'Fling',
    # artist: The artist of the song
    "artist": 'Jody',
    # album: The album name
    "album": 'Waves Ep',
    # album artist: The artist of the album
    "album_artist": 'Jody',
    # genre: The genre of the album
    "genre": 'wordwide',
    # year: The year the album was released
    "year": 2019,
    # total number of tracks: The total number of tracks the album has
    "total_number_of_tracks": 6,
    # rating: The current rating over 5 the album has
    "rating": 4,
    # is lyrics available: a boolean value indicating whether or not lyrics are available in the album
    "is_lyrics_available": True,
    # date released: The exact date the album was released
    # Note: the date is equated to the current date
    "date_released": datetime.datetime.now()
}

for data in album_data:
    # Print: Display all the attributes above
    print('Key: ', data+',', 'Value: ', album_data[data], '\n');

def guessGame(key, value):
    for data in album_data:
        #print('Data: ', data, 'key: ', key, 'Album value: ', album_data[data], 'value: ', value, 'keys equal: ', data == key, 'values equal: ', album_data[data] == value, 'if condition: ', data == key == album_data[data] == value)
        if data == key and album_data[data] == value:
            return True
        
    return False

print(guessGame("rating", 5))
print(guessGame("is_lyrics_available", True))
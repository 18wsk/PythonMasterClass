# prints list in ( )
# it is optional to define them in ( ) though -> safer to however

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Emilda May", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984), # put comma at end!!
          ]

print(len(albums))

for album_name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(album_name, artist, year))

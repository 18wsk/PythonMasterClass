from nested_data import albums

SONGS_LIST_INDEX = 3 #constants are written in all caps -> Dont change them at all
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exist):")
    for index, (title, artist, year, songs) in enumerate(albums):
        # must unpack in brackets since enumerate only returns 2 values
        # index and a value
        print("{}: {}"
              .format(index + 1, title))

    album_choice = int(input())
    if 1 <= album_choice <= len(albums):
        songs_list = albums[album_choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please Choose your song: ")
    for index, (track_number, song_title) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song_title))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        song = songs_list[song_choice-1][SONG_TITLE_INDEX]
        print("Playing: {}\n".format(song))

    print("="*80)








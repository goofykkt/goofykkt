def make_album(artist=None, ablum_title=None,number_of_songs = None):
    if number_of_songs:
        album ={'Artist':artist, 'Album Title':ablum_title,"Number of songs": number_of_songs }
    else:
        album = {'Artist':artist, 'Album Title':ablum_title}
    return print(album)


while True:
    artist = input("Insert the artist name or q to quit: ").title()
    if artist.lower() == 'q':
        break 
    album = input("Insert the album name or q to quit: ").title()
    if album.lower() == 'q':
        break
    songs = input("Insert the number of songs or leave it empty or q to quit").title()
    if songs.lower() == 'q':
        break
    make_album(artist,album,songs)

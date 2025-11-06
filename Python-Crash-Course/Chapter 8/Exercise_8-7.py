def make_album(artist, ablum_title,number_of_songs = None):
    if number_of_songs:
        album ={'Artist':artist, 'Album Title':ablum_title,"Number of songs": number_of_songs }
    else:
        album = {'Artist':artist, 'Album Title':ablum_title}
    return print(album)


# Examples with number of songs
album1 = make_album("Aurora Sky", "Neon Horizons", 12)
album2 = make_album("Echoes Fall", "Glass Hearts and Satellites", 11)

# Examples without number of songs
album3 = make_album("Silver Tide", "Midnight Concrete")
album4 = make_album("Crimson Pulse", "Binary Bloom")

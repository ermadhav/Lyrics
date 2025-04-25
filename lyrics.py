import lyricsgenius

genius = lyricsgenius.Genius(api_key)

name = input("Enter Artist Name: ")
song_title = input("Enter Song Title: ")

# Search for the song directly using artist and song name
song = genius.search_song(song_title, name)

if song:
    print(song.lyrics)
else:
    print("Song not found.")
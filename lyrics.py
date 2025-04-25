from flask import Flask, render_template, request, redirect, url_for
import lyricsgenius  # Make sure to install the lyricsgenius library

app = Flask(__name__)

# Initialize Genius API client with a valid access token
genius = lyricsgenius.Genius("jTk1u6luBLwPvflNUcYdfqY46YkLeFQLecTT3JjWaafjb-f9bLAt-AkTdJbWZJI5 ")  # Update with your new token

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        artist_name = request.form['artist']
        song_title = request.form['title']
        
        # Search for the song lyrics
        song = genius.search_song(song_title, artist_name)
        if song:
            return redirect(url_for('lyrics', artist=artist_name, title=song_title, lyrics=song.lyrics))
        else:
            return render_template('index.html', error="Lyrics not found!")
    
    return render_template('index.html')

@app.route('/lyrics')
def lyrics():
    artist = request.args.get('artist')
    title = request.args.get('title')
    lyrics = request.args.get('lyrics')
    
    return render_template('lyrics.html', artist=artist, title=title, lyrics=lyrics)

if __name__ == '__main__':
    app.run(debug=True)

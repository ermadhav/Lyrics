from flask import Flask, render_template, request, redirect, url_for
import lyricsgenius  # You can use the Genius API to get lyrics

app = Flask(__name__)

# Initialize Genius API client
genius = lyricsgenius.Genius("your_genius_api_key")

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

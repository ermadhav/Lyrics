from flask import Flask, render_template, request
import lyricsgenius

app = Flask(__name__)
genius = lyricsgenius.Genius("jTk1u6luBLwPvflNUcYdfqY46YkLeFQLecTT3JjWaafjb-f9bLAt-AkTdJbWZJI5")

@app.route("/", methods=["GET", "POST"])
def index():
    lyrics = ""
    if request.method == "POST":
        artist = request.form["artist"]
        title = request.form["title"]
        try:
            song = genius.search_song(title, artist)
            if song:
                lyrics = song.lyrics
            else:
                lyrics = "Lyrics not found."
        except Exception as e:
            lyrics = f"Error: {str(e)}"
    return render_template("index.html", lyrics=lyrics)

if __name__ == "__main__":
    app.run(debug=True)

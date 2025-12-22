from flask import Flask, jsonify
import csv
app = Flask(__name__)
class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres
movies = []
with open("movies.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie = Movie(row["movieId"], row["title"], row["genres"])
        movies.append(movie)

@app.route("/movies")
def get_movies():
    serialized = [movie.__dict__ for movie in movies]
    return jsonify(serialized)
@app.route("/")
def home():
    return "Serwer działa! Przejdź do /movies, aby zobaczyć listę filmów."

if __name__ == "__main__":
    app.run()
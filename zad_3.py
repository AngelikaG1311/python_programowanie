from flask import Flask, jsonify
import csv
app = Flask(__name__)
class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres
class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId
class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp
class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = int(timestamp)
movies = []
links = []
ratings = []
tags = []
with open("movies.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie = Movie(row["movieId"], row["title"], row["genres"])
        movies.append(movie)
with open("links.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        links.append(Link(row["movieId"], row["imdbId"], row["tmdbId"]))
with open("ratings.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ratings.append(Rating(row["userId"], row["movieId"], row["rating"], row["timestamp"]))
with open("tags.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tags.append(Tag(row["userId"], row["movieId"], row["tag"], row["timestamp"]))

@app.route("/movies")
def get_movies():
    serialized = [movie.__dict__ for movie in movies]
    return jsonify(serialized)
@app.route("/links")
def get_links():
    return jsonify([link.__dict__ for link in links])
@app.route("/ratings")
def get_ratings():
    return jsonify([rating.__dict__ for rating in ratings])
@app.route("/tags")
def get_tags():
    return jsonify([tag.__dict__ for tag in tags])
@app.route("/")
def home():
    return ("Serwer działa! Przejdź do /movies, aby zobaczyć listę filmów.\n"
            "Przejdź do /links, aby zobaczyć listę linków. \n"
            "Przejdź do /ratings, aby zobaczyć listę rankingów. \n"
            "Przejdź do /tags, aby zobaczyć listę tagów. \n")
if __name__ == "__main__":
    app.run()
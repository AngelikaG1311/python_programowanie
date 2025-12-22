import sqlite3
import csv
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

with open("movies.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO movies (movieId, title, genres)
            VALUES (?, ?, ?)
        """, (int(row["movieId"]), row["title"], row["genres"]))
with open("links.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO links (movieId, imdbId, tmdbId)
            VALUES (?, ?, ?)
        """, (int(row["movieId"]), row["imdbId"], row["tmdbId"]))
with open("ratings.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO ratings (userId, movieId, rating, timestamp)
            VALUES (?, ?, ?, ?)
        """, (int(row["userId"]), int(row["movieId"]), float(row["rating"]), int(row["timestamp"])))
with open("tags.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO tags (userId, movieId, tag, timestamp)
            VALUES (?, ?, ?, ?)
        """, (int(row["userId"]), int(row["movieId"]), row["tag"], int(row["timestamp"])))
conn.commit()
conn.close()
print("Dane zostały załadowane do bazy!")


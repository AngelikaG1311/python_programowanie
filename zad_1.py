import sqlite3
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    movieId INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genres TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS links (
    movieId INTEGER PRIMARY KEY,
    imdbId TEXT,
    tmdbId TEXT,
    FOREIGN KEY(movieId) REFERENCES movies(movieId)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings (
    userId INTEGER,
    movieId INTEGER,
    rating REAL,
    timestamp INTEGER,
    PRIMARY KEY(userId, movieId),
    FOREIGN KEY(movieId) REFERENCES movies(movieId)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tags (
    userId INTEGER,
    movieId INTEGER,
    tag TEXT,
    timestamp INTEGER,
    PRIMARY KEY(userId, movieId, tag),
    FOREIGN KEY(movieId) REFERENCES movies(movieId)
)
""")
conn.commit()
conn.close()
print("Baza danych i tabele zostały utworzone!")
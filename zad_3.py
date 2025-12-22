from flask import Flask, jsonify
import sqlite3
app = Flask(__name__)
DB_PATH = "movies.db"
def query_db(query):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
@app.route("/movies")
def get_movies():
    return jsonify(query_db("SELECT * FROM movies"))
@app.route("/links")
def get_links():
    return jsonify(query_db("SELECT * FROM links"))
@app.route("/ratings")
def get_ratings():
    return jsonify(query_db("SELECT * FROM ratings "))
@app.route("/tags")
def get_tags():
    return jsonify(query_db("SELECT * FROM tags"))
if __name__ == "__main__":
    app.run()

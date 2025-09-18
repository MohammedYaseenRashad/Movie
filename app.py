from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# List of genres to render in sidebar
GENRES = [
    "Recently Released", "Action", "Horror", "Comedy", "Drama", "Sci-fi", "Thriller",
    "Crime", "Romance", "Fantasy", "Animation", "Mystery", "Documentary", "Adventure"
]

# Home page
@app.route('/')
def home():
    return render_template('index.html', genres=GENRES, movies=[])

# Handle filter form submission
@app.route('/filter', methods=['POST'])
def filter_movies():
    selected_genres = request.form.getlist('genre')

    if not selected_genres:
        return render_template('index.html', genres=GENRES, movies=[])

    placeholders = ','.join('?' for _ in selected_genres)
    query = f"SELECT * FROM movies WHERE genre IN ({placeholders})"

    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute(query, selected_genres)
    movies = c.fetchall()
    conn.close()

    return render_template('index.html', genres=GENRES, movies=movies)

# Handle search
@app.route('/search', methods=['GET'])
def search_movies():
    query = request.args.get('query', '').strip()

    if not query:
        return render_template('index.html', genres=GENRES, movies=[])

    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE title LIKE ?", ('%' + query + '%',))
    movies = c.fetchall()
    conn.close()

    return render_template('index.html', genres=GENRES, movies=movies)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from models.Movie import load_movies_from_file
from models.Link import load_links_from_file
from models.Rating import load_ratings_from_file
from models.Tag import load_tags_from_file


movies_arr = load_movies_from_file('./data/movies.csv')
links_arr = load_links_from_file('./data/links.csv')
ratings_arr = load_ratings_from_file('./data/ratings.csv')
tags_arr = load_tags_from_file('./data/tags.csv')

app = Flask(__name__)


@app.route("/test")
def hello_world():
    return "Hello World"


@app.route("/movies")
def movies():
    return [movie.__dict__ for movie in movies_arr]


@app.route("/links")
def links():
    return [link.__dict__ for link in links_arr]


@app.route("/ratings")
def ratings():
    return [rating.__dict__ for rating in ratings_arr]


@app.route("/tags")
def tags():
    return [tag.__dict__ for tag in tags_arr]

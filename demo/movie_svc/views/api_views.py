from responder import Response

from app_instance import api
from data import db

response_count_max = 10


@api.route("/api/search/{keyword}")
def search_keyword(req, resp, keyword: str):
    movies = db.search_keyword(keyword)
    print(f"Searching for {keyword}, {len(movies)} results")

    limited = len(movies) > response_count_max
    if limited:
        movies = movies[:response_count_max]

    movie_dicts = [
        db.movie_to_dict(m)
        for m in movies
    ]

    resp.media = {'keyword': keyword, 'hits': movie_dicts, 'truncated_results': limited}


@api.route("/api/director/{director_name}")
def search_director(_, resp, director_name: str):
    movies = db.search_director(director_name)
    print(f"Searching for director {director_name}, {len(movies)} results")

    limited = len(movies) > response_count_max
    if limited:
        movies = movies[:response_count_max]

    movies_dicts = [
        db.movie_to_dict(m)
        for m in movies
    ]

    resp.media = {'keyword': director_name, 'hits': movies_dicts, 'truncated_results': limited}


@api.route("/api/movie/genre/{genre}")
def movies_by_genre(_, resp: Response, genre: str):
    hits = db.movies_by_genre(genre)
    print(f"Searching for movies by genre {genre}, {len(hits)} results")

    limited = len(hits) > response_count_max
    if limited:
        hits = hits[:response_count_max]

    hits_dicts = [
        db.movie_to_dict(m)
        for m in hits
    ]

    resp.media = {'genre': genre, 'hits': hits_dicts, 'truncated_results': limited}


@api.route("/api/movie/{imdb_number}")
def search_imdb(_, resp, imdb_number: str):
    movie = db.find_by_imdb(imdb_number)
    print(f"Looking up movie by code: {imdb_number}, found? {'Yes' if movie else 'NO'}")

    resp.media = db.movie_to_dict(movie)


@api.route("/api/movie/top")
def top_movies(_, resp: Response):
    hits = db.movies_by_popularity()

    limited = len(hits) > response_count_max
    if limited:
        hits = hits[:response_count_max]

    hits_dicts = [
        db.movie_to_dict(m)
        for m in hits
    ]

    keyword = f"top_{response_count_max}"

    resp.media = {'keyword': keyword, 'hits': hits_dicts, 'truncated_results': limited}


@api.route("/api/movie/genre/all")
def all_genres(_, resp: Response):
    resp.media = db.all_genres()

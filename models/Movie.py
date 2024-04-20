class Movie:
    def __init__(self, movie_id, title, genres):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres

def load_movies_from_file(file_path: str, separator: str = ",") -> list:
    movies = []
    with open(file_path, 'r', encoding = 'utf-8') as file:
        for line in file:
            movie_properties = line.strip().split(separator)
            id = movie_properties[0]
            title = ''
            if len(movie_properties) > 3:
                title = ''.join(movie_properties[1:-1]).strip('"')
            else:
                title = movie_properties[1]
            genres = movie_properties[-1]

            movie = Movie(id, title, genres)
            movies.append(movie)
    return movies

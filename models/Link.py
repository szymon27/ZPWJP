class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id


def load_links_from_file(file_path: str, separator: str = ",") -> list:
    links = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            link_properties = line.strip().split(separator)
            movie_id = link_properties[0]
            imdb_id = link_properties[1]
            tmdb_id = link_properties[2]
            link = Link(movie_id, imdb_id, tmdb_id)
            links.append(link)
    return links

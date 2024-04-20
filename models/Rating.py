class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

def load_ratings_from_file(file_path: str, separator: str = ",") -> list:
    ratings = []
    with open(file_path, 'r', encoding = 'utf-8') as file:
        for line in file:
            rating_properties = line.strip().split(separator)
            user_id = rating_properties[0]
            movie_id = rating_properties[1]
            rating = rating_properties[2]
            timestamp = rating_properties[3]
            link = Rating(user_id, movie_id, rating, timestamp)
            ratings.append(link)
    return ratings

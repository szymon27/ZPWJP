class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

def load_tags_from_file(file_path: str, separator: str = ",") -> list:
    tags = []
    with open(file_path, 'r', encoding = 'utf-8') as file:
        for line in file:
            tag_properties = line.strip().split(separator)
            user_id = tag_properties[0]
            movie_id = tag_properties[1]
            tag = tag_properties[2]
            timestamp = tag_properties[3]
            link = Tag(user_id, movie_id, tag, timestamp)
            tags.append(link)
    return tags

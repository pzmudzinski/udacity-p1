class Movie:

    def __init__(self, json):
        self.title = json["title"]
        self.poster_image_url = json["poster_url"]
        self.trailer_youtube_url = json["trailer_url"]
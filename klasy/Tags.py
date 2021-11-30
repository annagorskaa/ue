import datetime


class Tags:
    def __init__(self, userId: str, movieId: str, tag: str, timestamp: datetime):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

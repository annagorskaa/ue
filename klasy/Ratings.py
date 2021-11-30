import datetime


class Ratings:
    def __init__(self, userId: str, movieId: str, rating: float, timestamp: datetime):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

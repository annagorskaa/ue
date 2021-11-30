from flask import Flask
from flask_restful import Resource, Api
from Metody.Movies import get_movies
from Metody.Links import get_links
from Metody.Ratings import get_ratings
from Metody.Tags import get_tags

app = Flask(__name__)
api = Api(app)


class Movies(Resource):
    def get(self):
        return get_movies()


api.add_resource(Movies, '/movies')


class Links(Resource):
    def get(self):
        return get_links()


api.add_resource(Links, '/links')


class Ratings(Resource):
    def get(self):
        return get_ratings()


api.add_resource(Ratings, '/ratings')


class Tags(Resource):
    def get(self):
        return get_tags()


api.add_resource(Tags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, Response
from database.models import Movie
from flask_restful import Resource


class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        _id = movie.id
        return {'id': str(_id)}, 200


class MovieApi(Resource):
    def update(self, _id: str):
        body = request.get_json()
        Movie.objects.get(id=_id).update(**body)
        return '', 200

    def delete(self, _id):
        Movie.objects.get(id=_id).delete()
        return '', 200

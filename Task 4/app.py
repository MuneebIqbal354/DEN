from flask import Flask, jsonify, request
import random

ratings = [1,2,3,4,5,6,7,8,9,10]

app = Flask(__name__)

#Sample data

movies = [
    {"Title": "Avengers End Game", "Rating": 4, "Gener": "Action, Sci-fi"},
    {"Title": "Iron man", "Rating": 7, "Gener": "Action, Adventure"},
    {"Title": "Batman Beigns", "Rating": 9, "Gener": "Action, Thriller, Adventure"},
    {"Title": "Captain America", "Rating": 6, "Gener": "Action, Thriller"}
]


# To run the api
@app.route('/movies', methods=['GET'])
def get_movies():
    return movies


# To read the data
@app.route('/movies/<string:movies_Title>', methods = ['GET'])
def movie_title(movies_Title):
    for movie in movies:
        if movie['Title'] == movies_Title:
            return movie
    return {'Error':'Not Found'}

# Add a New Movie
@app.route('/movies', methods=['POST'])
def add_movie():
    new_movie = {'Title': request.json['Title'], 'Rating': random.choice(ratings), 'Gener': request.json['Gener']}
    movies.append(new_movie)
    return new_movie

# Update Movie Ratings
@app.route('/movies/<string:movies_Title>', methods = ['PUT'])
def update_movie(movies_Title):
    for film in movies:
        if film['Title'] == movies_Title:
            # film['Title'] = request.json['Title']
            film['Rating'] = request.json['Rating']
            return film
    return {"Error": "Movie not found"}


# Delete a movie
@app.route('/movies/<string:movies_Title>', methods = ['DELETE'])
def delete_movie(movies_Title):
    for film in movies:
        if film['Title'] == movies_Title:
            movies.remove(film)
            return {"data": "Movie Deleted Successfully"}
    return {"Error": "Movie not found"}

# Run Flask App
if __name__=='__main__':
    app.run(debug=True)
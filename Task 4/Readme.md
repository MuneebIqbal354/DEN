<h1 align="center">Task No. 4: RESTful API with Flask</h1>


This project is about a RESTful API built using Flask, which allows users to perform CRUD (Create, Read, Update, Delete) operations on a list of movies. Below i have explained how the code works.

## Code

### Imports

- **Flask:** This is the main framework used to build the API.
- **jsonify:** Converts Python dictionaries to JSON format for API responses.
- **request:** Used to access data sent by the client (like adding or updating movies).
- **random:** A Python module to assign a random rating to newly added movies.

```python
from flask import Flask, jsonify, request
import random
```
### Sample Data

- A list of movie dictionaries serves as our in-memory database. Each movie contains `Title`, `Rating`, and `Genre`.

```python
movies = [
    {"Title": "Avengers End Game", "Rating": 4, "Gener": "Action, Sci-fi"},
    {"Title": "Iron man", "Rating": 7, "Gener": "Action, Adventure"},
    {"Title": "Batman Beigns", "Rating": 9, "Gener": "Action, Thriller, Adventure"},
    {"Title": "Captain America", "Rating": 6, "Gener": "Action, Thriller"}
]
```

### Getting All Movies

- **Endpoint:** `/movies`
- **Method:** `GET`
- **Function:** Returns the full list of movies in JSON form

```python
@app.route('/movies', methods=['GET'])
def get_movies():
    return movies
```

<img width="960" alt="Screenshot 2024-10-01 195023" src="https://github.com/user-attachments/assets/70f94953-c509-478b-b585-2d59034c0a5c">


### Getting a Movie by Title

- **Endpoint:** `/movies/<string:movies_Title>`
- **Method:** `GET`
- **Function:** Retrieves a movie based on its title. If the movie is not found, it returns an error message.

```python
@app.route('/movies/<string:movies_Title>', methods=['GET'])
def movie_title(movies_Title):
    for movie in movies:
        if movie['Title'] == movies_Title:
            return movie
    return {'Error': 'Not Found'}
```

<img width="960" alt="Screenshot 2024-10-01 201349" src="https://github.com/user-attachments/assets/cd63c38e-54ec-48d4-ae1a-dcb6b065434f">


### Adding a New Movie

- **Endpoint:** `/movies`
- **Method:** `POST`
- **Function:** Adds a new movie to the list using the `Title` and `Gener` from the request body, while assigning a random `Rating`.

```python
@app.route('/movies', methods=['POST'])
def add_movie():
    new_movie = {'Title': request.json['Title'], 'Rating': random.choice(ratings), 'Gener': request.json['Gener']}
    movies.append(new_movie)
    return new_movie
```

<img width="960" alt="Screenshot 2024-10-01 204543" src="https://github.com/user-attachments/assets/fd3e6fdb-1b35-4536-b224-129dc8e54e6f">

<img width="960" alt="Screenshot 2024-10-01 204721" src="https://github.com/user-attachments/assets/54e75f6b-25b1-48eb-82c4-b43b5001b8c3">


### Updating Movie Rating

- **Endpoint:** `/movies/<string:movies_Title>`
- **Method:** `PUT`
- **Function:**  Updates the rating of an existing movie. If the movie is not found, it returns an error message.

```python
@app.route('/movies/<string:movies_Title>', methods=['PUT'])
def update_movie(movies_Title):
    for film in movies:
        if film['Title'] == movies_Title:
            film['Rating'] = request.json['Rating']
            return film
    return {"Error": "Movie not found"}
```

![Screenshot 2024-10-02 002632](https://github.com/user-attachments/assets/febb8318-e256-4f81-a826-edbfccaa799a)

### Deleting a Movie

- **Endpoint:** `/movies/<string:movies_Title>`
- **Method:** `DELETE`
- **Function:**  Deletes a movie from the list based on its title. If the movie is not found, it returns an error.

```python
@app.route('/movies/<string:movies_Title>', methods=['DELETE'])
def delete_movie(movies_Title):
    for film in movies:
        if film['Title'] == movies_Title:
            movies.remove(film)
            return {"data": "Movie Deleted Successfully"}
    return {"Error": "Movie not found"}
```

![Screenshot 2024-10-02 012040](https://github.com/user-attachments/assets/b68895b0-9ceb-4535-809b-df86f62b1466)

![Screenshot 2024-10-02 012121](https://github.com/user-attachments/assets/8ca0cca5-cbdb-4f21-b286-f3153df55628)

### Running the Flask Application

- This runs the Flask application in debug mode, making it easier to catch errors and debug the API while developing.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

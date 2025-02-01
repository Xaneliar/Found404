from flask import Flask, render_template, request, redirect, url_for
from assets.api_key import API_KEY
import Models.Movie_Recommendations as Movie_Recommendations
import Models.Shows_Recommendations as Shows_Recommendations
import serpapi

app = Flask(__name__)

def GET_MoviePosters(movie):
    movies = Movie_Recommendations.get_recommendations(movie).tolist()
    movie_dict = {}
    for i in movies:
        params = {
        "q": i,
        "engine": "google_images",
        "hl": 'en',
        "ijn": "0",
        "api_key": API_KEY
        }
        search = serpapi.search(params)
        if 'images_results' in search and search['images_results']:
            image_link = search['images_results'][0]['original']
            movie_dict[i] = image_link  # Store the movie name as key and image link as value
        else:
            movie_dict[i] = "No Image Found"  # If no image is found, mark as "No Image Found"
    
    return movie_dict

def GET_ShowsPosters(show):
    shows = Shows_Recommendations.get_recommendations(show).tolist()
    show_dict = {}
    for i in shows:
        params = {
        "q": i,
        "engine": "google_images",
        "hl": 'en',
        "ijn": "0",
        "api_key": API_KEY
        }
        search = serpapi.search(params)
        if 'images_results' in search and search['images_results']:
            image_link = search['images_results'][0]['original']
            show_dict[i] = image_link  # Store the movie name as key and image link as value
        else:
            show_dict[i] = "No Image Found"  # If no image is found, mark as "No Image Found"
    
    return show_dict

@app.route('/',methods=['GET'])
def index():
    return render_template('frontend/index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('frontend/loginpage.html')

@app.route('/choice', methods=['GET','POST'])
def choice():
    if request.method == 'POST':
        movie_name = request.form.get('movie_name')
        if movie_name:
            try:
                posters = GET_MoviePosters(movie_name)
                return redirect(url_for('movies', submitted=True, movie_name=movie_name))
            except Exception as e:
                return f"Error: {str(e)}", 500
        else:
            return "Movie name is required", 400
    return render_template('frontend/choice.html')


@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if request.method == 'POST':
        movie_name = request.form.get('movie_name')
        if movie_name:
            try:
                posters = GET_MoviePosters(movie_name)
                return render_template('frontend/Movies.html', posters=posters)
            except Exception as e:
                return f"Error: {str(e)}", 500
        else:
            return "Movie name is required", 400
    return render_template('frontend/Movies.html')

@app.route('/shows', methods=['GET', 'POST'])
def shows():
    if request.method == 'POST':
        show_name = request.form.get('show_name')
        if show_name:
            try:
                posters = GET_ShowsPosters(show_name)
                return render_template('frontend/shows.html', posters=posters)
            except Exception as e:
                return f"Error: {str(e)}", 500
        else:
            return "Show name is required", 400
    return render_template('frontend/shows.html')

if __name__ == '__main__':
    app.run(debug=True)
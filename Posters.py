import serpapi
import import_ipynb
from assets.api_key import API_KEY
import Models.Movie_Recommendations as Movie_Recommendations
import Models.Shows_Recommendations as Shows_Recommendations

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

def GET_ShowsPosters(movie):
    movies = Shows_Recommendations.get_recommendations(movie).tolist()
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

def available(movie):
    movies = Movie_Recommendations.get_recommendations(movie).tolist()
    linklist = []
    movie_names = []  # To store movie names
    for i in movies:
        movie_names.append(i)  # Add movie name to the list
        params = {
            "q": i,
            "engine": "google",
            "hl": 'en',
            "ijn": "0",
            "api_key": API_KEY
        }

        search = serpapi.search(params)
        if 'available_on' in search:
            links = search['available_on']
            links_thumbnails = [(item['link'], item['thumbnail']) for item in links]
            linklist.append(links_thumbnails)
        else:
            linklist.append("Not Available")
    
    # Return a dictionary with 'name' and 'poster' keys
    return {'name': movie_names, 'poster': linklist}

        


    
import serpapi
from assets.api_key import API_KEY

def GenreMixing(genre1, genre2):
    query = genre1 + ' ' + genre2 + "Movies"
    params = {
            "q": query,
            "engine": "google",
            "hl": 'en',
            "ijn": "0",
            "api_key": API_KEY
            }
    search = serpapi.search(params)
    if 'knowledge_graph' in search:
        result = search['knowledge_graph']
        posters = list(result.values())[0]
        posters_list = [i['image'] for i in posters]
        return posters_list
    else:
        return "Not Available"
    
if __name__ == "__main__":
    genre1 = input("Enter Genre 1: ")
    genre2 = input("Enter Genre 2: ")
    print(GenreMixing(genre1,genre2))
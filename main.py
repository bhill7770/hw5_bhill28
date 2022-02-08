import requests
import os


BASE_URL = "https://api.themoviedb.org/3"

trending_movies_result = requests.get(f"{BASE_URL}/movie/popular", params={'api_key': os.getenv("API_KEY")})
data = trending_movies_result.json()

for pop_movie in data["results"]:
    
    Movie_title = pop_movie['title']
    brief_summary = pop_movie['overview']
    
    print("Currently Trending Movie Title: " + Movie_title)
    print("Synopsis: " + brief_summary[:100] + "...")
    print()

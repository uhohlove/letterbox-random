from letterboxdpy.list import List
import random

username = input("Enter Letterboxd username: ")
list = input("Enter the list name (copy after /list/ in url): ")
print(f"Grabbing movies from {username}'s list...")

list_instance = List(username, list)

movie_list = []
for movie_id, movie in list_instance.movies.items():
    if "name" in movie:
        title_year = f"{movie['name']} ({movie.get('year', 'N/A')})"
        movie_list.append(title_year)
if len(movie_list) > 0:
    selected_movie = random.choice(movie_list)
    print(f"\n Selected Movie: {selected_movie}")
else:
    print("Couldn't find movies/list")

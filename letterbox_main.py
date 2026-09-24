from letterboxdpy.list import List
from letterboxdpy.watchlist import Watchlist
from letterboxdpy import movie
from letterboxdpy.movie import movie_profile
import random

import random
from letterboxdpy import movie
from letterboxdpy.list import List

username = input("Enter Letterboxd username: ")
list_name = input("Enter the list name (copy after /list/ in url): ")
print(f"Grabbing movies from {username}'s list...")

list_instance = List(username, list_name)

movie_list = []
for movie_id, mov in list_instance.movies.items():
  if "name" in mov and "slug" in mov:
    # Keep track of both name and slug
    movie_info = {"name": mov["name"], "slug": mov["slug"]}
    movie_list.append(movie_info)

if len(movie_list) > 0:
  # Pick a random movie dictionary
  selected = random.choice(movie_list)
  title = selected["name"]
  slug = selected["slug"]

  print(f"\n🎲 Selected Movie: {title}")

# Fetch the movie profile using its unique slug
try:
      movie_obj = movie.Movie(slug)

      if hasattr(movie_obj, "genres") and movie_obj.genres:
        # Filter to ONLY include items where type is 'genre'
        pure_genres = [
            item["name"] for item in movie_obj.genres if item.get("type") == "genre"
        ]

        print(f"🎬 Genres: {', '.join(pure_genres)}")
      else:
        print("🎬 Genres: Not found")

except Exception as e:
      print(f"Could not fetch genres for this movie: {e}")
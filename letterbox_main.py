import random
from letterboxdpy import movie
from letterboxdpy.list import List

username = input("Enter Letterboxd username: ")
list_name = input("Enter the list name (copy after /list/ in url): ")
target_genre = input(
    "Enter a genre to filter by (e.g., Science Fiction, Action, Comedy): "
).strip().lower()

print(f"\nGrabbing and filtering movies from {username}'s list...")

list_instance = List(username, list_name)

matching_movies = []

for movie_id, mov in list_instance.movies.items():
  if "name" in mov and "slug" in mov:
    title = mov["name"]
    slug = mov["slug"]

    try:
      # Fetch the movie profile to check its genres
      movie_obj = movie.Movie(slug)
      if hasattr(movie_obj, "genres") and movie_obj.genres:
        # Extract just the pure genre names and make them lowercase for a safe match
        pure_genres = [
            item["name"].lower()
            for item in movie_obj.genres
            if item.get("type") == "genre"
        ]

        # If the target genre is in this movie's genres, add it to our pool
        if target_genre in pure_genres:
          matching_movies.append({"name": title, "slug": slug})
    except Exception:
      # Skip movies that throw errors during lookup
      continue

# Pick a random movie from the filtered list, if any match
if len(matching_movies) > 0:
  selected = random.choice(matching_movies)
  print(
      f"\n🎲 Random {target_genre.title()} Movie Selected: {selected['name']}"
  )
else:
  print(
      f"\n❌ No movies found matching the genre '{target_genre}' in this list."
  )
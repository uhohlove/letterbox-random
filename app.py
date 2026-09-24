from letterboxdpy.list import List
from letterboxdpy.watchlist import Watchlist
from letterboxdpy.films import get_movies_by_genre
import random
import streamlit as st

st.title("Letterboxd Random Movie Gen")
st.header("Leave list box empty for user's watchlist")
username = st.text_input("Enter Letterboxd username: ")
list = st.text_input("Enter the list name (copy after /list/ in url): ")

#Function for loading the movies into empty movie list and picking a random movie from list 
def list_grabber():
        try:
            with st.spinner(f"Grabbing movies from {username}'s list..."):
                list_instance = List(username, list)
                movie_list = []
                for movie_id, movie in list_instance.movies.items():
                    if "name" in movie:
                        title_year = f"{movie['name']} ({movie.get('year', 'N/A')})"
                        movie_list.append(title_year)
            if (len(movie_list) > 0):
                selected_movie = random.choice(movie_list)
                st.success(f"Selected Movie: {selected_movie}")
            else:
                st.warning("Couldn't find movies/list")
        except Exception as e:
            st.error(f"Error grabbing list: {e}")

def watchlist_grabber():
        try:
            with st.spinner(f"Grabbing movies from {username}'s watchlist..."):
                watchlist_instance = Watchlist(username)
                movie_list = []
                for movie_id, movie in watchlist_instance.movies.items():
                    if "name" in movie:
                        title_year = f"{movie['name']} ({movie.get('year', 'N/A')})"
                        movie_list.append(title_year)
            if (len(movie_list) > 0):
                selected_movie = random.choice(movie_list)
                st.success(f"Selected Movie: {selected_movie}")
            else:
                st.warning("Couldn't find movies/list")
        except Exception as e:
            st.error(f"Error grabbing watchlist for user: {username}")

def genre_list_grabber(target_genre):
        try:
            with st.spinner(f"Grabbing {target_genre} movies from {username}'s list"):
                list_instance = List(username, list)
                movie_list = []

                for movie_id, mov in list_instance.movies.items():
                    if "name" in mov and "slug" in mov:
                        title = mov["name"]
                        slug = mov["slug"]
                        try:
                            movie_obj = movie.Movie(slug)
                            if hasattr(movie_obj, "genres") and movie_obj.genres:
                                match_genres = [
                                    item["name"].lower()
                                    for item in movie_obj.genres
                                    if item.get("type") == "genre"
                                ]
                                if target_genre.lower() in match_genres:
                                    movie_list.append({"name": title, "slug": slug})
                        except Exception: continue
            if (len(movie_list) > 0):
                selected_movie = random.choice(movie_list)
                st.success(f"Selected Movie: {selected_movie}")
            else:
                st.warning("Couldn't find movies/list")
        except Exception as e:
            st.error(f"Error grabbing list")

if st.button("Random Movie"):
    if username and list:
        list_grabber()
    elif username and not list:
        watchlist_grabber()
    else: 
        st.warning("Fill in necessary fields")
if st.button("Random Comedy"):
    if username and list:
        genre_list_grabber("comedy")

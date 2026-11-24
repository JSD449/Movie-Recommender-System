import streamlit as st
from collections import Counter

# Page Setup
st.set_page_config(page_title="Movie Recommender Prototype", layout="wide")

# Mock Movie Catalogue (Simulated Data)
MOVIES = [
    {"id": 1, "title": "Outer Orbit", "genres": ["Sci-Fi", "Adventure"], "year": 2021, "series": "Outer Orbit", "series_role": "Original"},
    {"id": 2, "title": "Outer Orbit 2", "genres": ["Sci-Fi", "Adventure", "Action"], "year": 2024, "series": "Outer Orbit", "series_role": "Sequel"},
    {"id": 3, "title": "Outer Orbit: Zero", "genres": ["Sci-Fi", "Action"], "year": 2023, "series": "Outer Orbit", "series_role": "Prequel"},
    {"id": 4, "title": "Vanguard Rising", "genres": ["Superhero", "Action"], "year": 2019, "series": "Vanguard Universe", "series_role": "Original"},
    {"id": 5, "title": "Iron Sentinel", "genres": ["Superhero", "Action", "Sci-Fi"], "year": 2020, "series": "Vanguard Universe", "series_role": "Same Universe"},
    {"id": 6, "title": "Shadow Knight", "genres": ["Superhero", "Action", "Mystery"], "year": 2022, "series": "Vanguard Universe", "series_role": "Same Universe"},
    {"id": 7, "title": "Vanguard: Endgame", "genres": ["Superhero", "Action", "Romance"], "year": 2025, "series": "Vanguard Universe", "series_role": "Sequel"},
    {"id": 8, "title": "Play Time", "genres": ["Animation", "Comedy", "Family"], "year": 2012, "series": "Play Time", "series_role": "Original"},
    {"id": 9, "title": "Play Time: Road Trip", "genres": ["Animation", "Comedy"], "year": 2015, "series": "Play Time", "series_role": "Sequel"},
    {"id": 10, "title": "Cold", "genres": ["Animation", "Adventure"], "year": 2020, "series": None, "series_role": None},
    {"id": 11, "title": "Departure", "genres": ["Drama", "Romance"], "year": 2017, "series": None, "series_role": None},
    {"id": 12, "title": "The In Laws", "genres": ["Drama", "Family"], "year": 2021, "series": None, "series_role": None},
    {"id": 13, "title": "Office Mayhem", "genres": ["Comedy"], "year": 2019, "series": None, "series_role": None},
    {"id": 14, "title": "Weekend Alibi", "genres": ["Drama", "Mystery"], "year": 2023, "series": None, "series_role": None},
    {"id": 15, "title": "Getaway", "genres": ["Action", "Comedy"], "year": 2002, "series": "Getaway", "series_role": "Original"},
    {"id": 16, "title": "Getaway 2", "genres": ["Action", "Comedy"], "year": 2009, "series": "Getaway", "series_role": "Sequel"},
    {"id": 17, "title": "Getaway Lockdown", "genres": ["Action", "Comedy", "Mystery"], "year": 2021, "series": "Getaway", "series_role": "Sequel"},
    {"id": 18, "title": "Wedding by Sunset", "genres": ["Romance", "Comedy"], "year": 2026, "series": None, "series_role": None},
    {"id": 19, "title": "Super Strong", "genres": ["Superhero"], "year": 2012, "series": None, "series_role": None},
    {"id": 20, "title": "Stronger Together", "genres": ["Superhero", "Romance"], "year": 2018, "series": None, "series_role": None},
]

# Initialize Session State (Starting Watch History)
if "watch_history" not in st.session_state:
    # Outer Orbit, Vanguard Rising, Play Time, Departure
    st.session_state.watch_history = [1, 4, 8, 11]

# Helper Functions (Simulated Taste Profile & Recommendation Engine)
def get_movie_by_id(movie_id):
    return next((movie for movie in MOVIES if movie["id"] == movie_id), None)

def build_taste_profile(history_ids):
    genre_counts = Counter()
    watched_series = set()
    for movie_id in history_ids:
        movie = get_movie_by_id(movie_id)
        if movie:
            genre_counts.update(movie["genres"])
            if movie["series"]:
                watched_series.add(movie["series"])
    return genre_counts, watched_series

def get_recommendations(history_ids, top_n=8):
    genre_counts, watched_series = build_taste_profile(history_ids)
    candidates = [movie for movie in MOVIES if movie["id"] not in history_ids]

    def score_movie(movie):
        # Boost movies from a series/universe the user has already watched
        series_score = 3 if (movie["series"] and movie["series"] in watched_series) else 0
        # Add points for each matching genre in the taste profile
        genre_score = sum(genre_counts[genre] for genre in movie["genres"])
        return series_score + genre_score

    # changed so it only keeps in movies with at least one genre or series match  
    scored = [movie for movie in candidates if score_movie(movie) > 0]
    ranked = sorted(scored, key=score_movie, reverse=True)
    return ranked[:top_n]

def render_movie_grid(movie_list, show_watched_badge=False):
    cols = st.columns(4)
    for idx, movie in enumerate(movie_list):
        with cols[idx % 4]:
            with st.container(border=True):
                st.markdown(f"### {movie['title']}")
                if show_watched_badge and movie["id"] in st.session_state.watch_history:
                    st.caption("Watched")
                st.write(f"**Genres:** {', '.join(movie['genres'])}")
                st.write(f"**Year:** {movie['year']}")
                if movie["series"]:
                    st.caption(f"🔗 {movie['series']} ({movie['series_role']})")
                else:
                    st.caption("Standalone film")

# Sidebar: Inspect Simulated Taste Profile
genre_counts, watched_series = build_taste_profile(st.session_state.watch_history)
with st.sidebar:
    st.header("Simulated Taste Profile")
    st.caption("Generated automatically from your watch history.")
    if genre_counts:
        st.write("**Top Genres:**")
        for genre, count in genre_counts.most_common():
            st.write(f"- {genre} ({count})")
    if watched_series:
        st.write("**Watched Franchises:**")
        for s in sorted(watched_series):
            st.write(f"- {s}")

# Main UI
st.title("🎬 Movie Recommender Prototype")

tab_recs, tab_catalogue = st.tabs(["Recommended for You", "Full Catalogue"])

with tab_recs:
    st.subheader("Recommended for You")
    recommendations = get_recommendations(st.session_state.watch_history)
    if recommendations:
        render_movie_grid(recommendations)
    else:
        st.info("No personalized recommendations yet. Watch a movie from the Full Catalogue to build your taste profile.")

with tab_catalogue:
    st.subheader("Full Movie Catalogue")
    render_movie_grid(MOVIES, show_watched_badge=True)
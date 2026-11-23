import streamlit as st

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

# Main UI
st.title("🎬 Movie Recommender Prototype")
st.subheader("Movie Catalogue")

cols = st.columns(4)
for idx, movie in enumerate(MOVIES):
    with cols[idx % 4]:
        with st.container(border=True):
            st.markdown(f"### {movie['title']}")
            st.write(f"**Genres:** {', '.join(movie['genres'])}")
            st.write(f"**Year:** {movie['year']}")
            if movie["series"]:
                st.caption(f"🔗 {movie['series']} ({movie['series_role']})")
            else:
                st.caption("Standalone film")
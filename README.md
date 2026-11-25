#  Human Centred Movie Recommender Interactive System 

**README Prose Word Count:** ~540 words *(excluding code blocks and setup commands)*

## Project Status
An interactive Streamlit prototype exploring transparency, user control, and reversibility in personalised movie recommendation.

- **Implemented:**
  - User interface
  - 20-movie fictional catalogue with genre, release year, and franchise metadata.
  - Dynamic **"Why this?"** expanders on recommendation cards tracing franchise and genre matches back to specific watched films.
  - **Watch History** tab to view watched films, add new ones (`▶ Watch Movie`), remove items, and reverse deletions via a one-click **↩ Undo** banner.
  - Per-item **Use for recommendations** toggle to temporarily exclude watched films from recommendations without deleting them.
  - Global **Pause Watch History** toggle with a persistent status banner and notifications.
- **Simulated:**
  - Content-based recommendation engine (franchise boost + genre frequency scoring) with zero-score filtering.
  - Live **Simulated Taste Profile** sidebar.
  - Movie playback (triggered via button click) and in-memory persistence via `st.session_state` (reloading the browser resets the demo).
- **Unfinished / Planned:**
  - Persistent user accounts and database storage and real video streaming integration.
  - User supplied preferences that edit taste profile
  - Taste Change Evaluation

## Technology Stack
- **Python 3 & Streamlit:** Core application logic, UI layout, and in-memory session state (`st.session_state`).
- **Python `collections.Counter`:** Calculates live genre frequencies for the taste profile.
- **Git & GitHub:** Version control and staged development tracking.
- **Google Gemini:** AI assistant used for iterative prototyping, debugging, and documentation drafting.
- **Undecided Choices:** Machine Learning Recommendation Algorithm

## Running and Inspecting the Work
1. Download `app.py` from this repository (or clone it with `git clone https://github.com/JSD449/Movie-Recommender-System.git`).
2. Make sure Python 3 is installed, then install Streamlit:
   ```bash
   pip install streamlit
3. Use below command to run the code:
   ```bash
   streamlit run app.py

## Development Record
The prototype was built and tested across 10 stages:

- Stage 1 ([commit link](https://github.com/JSD449/Movie-Recommender-System/commit/025eac4d32ca43984f51cb558d2d7782db7a3abd)): Created the Streamlit app shell and 20-movie fictional catalogue. Checked layout rendering.

- Stage 2 ([commit link](https://github.com/JSD449/Movie-Recommender-System/commit/1600803397b33e4b07c2466debfff8530c724bee)): Added the simulated taste profile, recommendation scoring, and two-tab UI.

- Stage 3 ([commit link](https://github.com/JSD449/Movie-Recommender-System/commit/e8e80f7200cbbb21ab3ca0f9e7c6fb65e3a643f4)): Fixed an edge case where zero-score movies appeared in recommendations by filtering them out and adding an empty-state message.

- Stage 4 ([commit link](https://github.com/JSD449/Movie-Recommender-System/commit/14b3075ab35a7ba3fa5d0a0c244ccab48b72cec6)): Added dynamic "Why this?" transparency expanders. Verified explanations matched active watch history.

- Stage 5 ([commit link](https://github.com/JSD449/Movie-Recommender-System/commit/2e9f04bc723d1d793cdc270edc5a25eff5204572)): Added the Watch History tab and removal controls. Checked that removing a film immediately updated the sidebar and recommendations.

- Stage 6 ([commit link](https://github.com/JSD449/Movie-Recommender-System/commit/99a0f53efaba33d1be925053942cba9a8fe509e9)): Added the simulated ▶ Watch Movie button across both grids so adding and removing films could be tested end-to-end.

- Stage 7 ([commit link](https://github.com/JSD449/Movie-Recommender-System/commit/06ebb1f99fafc70e59d1ccd499d82c650e984977)): Added the ↩ Undo confirmation banner for reversible deletions.

- Stage 8 ([commit link](https://github.com/JSD449/Movie-Recommender-System/commit/35c49e01504c0f5a2b8b57be03ef37c020071b4e)): Added the Pause Watch History toggle, status banner, and notifications. Checked that watched films were not saved while paused.

- Stage 9 ([commit link](https://github.com/JSD449/Movie-Recommender-System/commit/31935e9cb295853db816b44874eb8be4a5c7cc10)): Added the Use for recommendations toggle to mute history items without deleting them.

- Stage 10: Did final changes and test and created README.

## AI Assistance
Tool Used: Google Gemini.

How It Was Used: Drafting and developing Streamlit UI code, debugging Python errors, and formatting this README.

Changes & Verification:

Chose to change the recommendation to not include titles that had no shared genre or series, add the ▶ Watch Movie button and made changes to ensure temporary exclusion of history items.

Tested every stage locally in Streamlit; caught and fixed state bugs (including a last_removeed session-state typo and missing parentheses on get_active_history()).

Verified that recommendations, explanations, and pause-tracking behaviour updated accurately after each change.

## Additional Files

No accompanying ZIP files are required; all prototype code (app.py) and documentation (README.md) are in this repository.
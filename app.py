import random
import streamlit as st
from logic_utils import (
    build_history_entry,
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    validate_guess_in_range,
)


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

# FIX: Detect difficulty changes and regenerate secret in the new range
if "last_difficulty" not in st.session_state:
    st.session_state.last_difficulty = difficulty
elif st.session_state.last_difficulty != difficulty:
    st.session_state.secret = random.randint(low, high)
    st.session_state.last_difficulty = difficulty

# FIX: Initialize attempts to 0 so first guess counts as attempt 1
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

# FIX: Show attempts left accounting for a press of Submit in this run
attempts_used = st.session_state.attempts + (1 if submit else 0)
st.info(
    f"Target range: {low} to {high}. "
    f"Attempts after this turn: {max(attempt_limit - attempts_used, 0)}"
)

# FIX: Use the selected difficulty's range instead of hardcoding 1-100
if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.history = []
    # FIX: Reset status to playing so the game unfreezes after a win or loss
    st.session_state.status = "playing"
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.error(err)
    else:
        in_range, range_err = validate_guess_in_range(guess_int, low, high)

        if not in_range:
            st.error(range_err)
        else:
            # FIX: Centralized numeric comparison keeps hints consistent.
            outcome, message = check_guess(guess_int, st.session_state.secret)
            st.session_state.history.append(
                build_history_entry(
                    attempt_number=st.session_state.attempts,
                    guess=guess_int,
                    outcome=outcome,
                    message=message,
                    secret=st.session_state.secret,
                )
            )

            if show_hint:
                if outcome == "Win":
                    st.success(message)
                elif outcome == "Too High":
                    st.warning(f"{message} Your guess was above the secret.")
                else:
                    st.info(f"{message} Your guess was below the secret.")

            st.session_state.score = update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=st.session_state.attempts,
            )

            if outcome == "Win":
                st.balloons()
                st.session_state.status = "won"
                st.success(
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                )
            else:
                if st.session_state.attempts >= attempt_limit:
                    st.session_state.status = "lost"
                    st.error(
                        f"Out of attempts! "
                        f"The secret was {st.session_state.secret}. "
                        f"Score: {st.session_state.score}"
                    )

st.subheader("Current Status")
status_col1, status_col2, status_col3 = st.columns(3)
with status_col1:
    st.metric("Score", st.session_state.score)
with status_col2:
    st.metric(
        "Attempts Left",
        max(attempt_limit - st.session_state.attempts, 0),
    )
with status_col3:
    st.metric("Difficulty", difficulty)

if st.session_state.history:
    st.subheader("Guess History")
    st.table(st.session_state.history)

st.subheader("Round Summary")
summary_data = {
    "Difficulty": difficulty,
    "Range": f"{low}-{high}",
    "Attempts Used": st.session_state.attempts,
    "Attempts Remaining": max(attempt_limit - st.session_state.attempts, 0),
    "Score": st.session_state.score,
    "Status": st.session_state.status.title(),
}
st.table([summary_data])

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")

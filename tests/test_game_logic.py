import sys
import random
import streamlit as st
from logic_utils import (
    build_history_entry,
    check_guess,
    describe_guess_distance,
    parse_guess,
    validate_guess_in_range,
)


def test_winning_guess():
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_guess_hint_uses_numeric_comparison():
    result = check_guess(51, 50)
    assert result == ("Too High", "📉 Go LOWER!")


def test_parse_guess_rejects_blank_input():
    result = parse_guess("")
    assert result == (False, None, "Enter a guess.")


def test_parse_guess_rejects_text_input():
    result = parse_guess("banana")
    assert result == (False, None, "That is not a number.")


def test_parse_guess_rejects_decimal_input():
    result = parse_guess("3.14")
    assert result == (False, None, "Please enter a whole number.")


def test_validate_guess_rejects_negative_number():
    result = validate_guess_in_range(-5, 1, 100)
    assert result == (False, "Guess must be between 1 and 100.")


def test_validate_guess_rejects_extremely_large_number():
    result = validate_guess_in_range(1000000, 1, 100)
    assert result == (False, "Guess must be between 1 and 100.")


def test_validate_guess_accepts_number_inside_range():
    result = validate_guess_in_range(42, 1, 100)
    assert result == (True, None)


def test_describe_guess_distance_labels_close_guesses():
    result = describe_guess_distance(47, 50)
    assert result == "Close"


def test_describe_guess_distance_labels_far_guesses():
    result = describe_guess_distance(10, 50)
    assert result == "Far"


def test_build_history_entry_includes_attempt_guess_result_and_distance():
    result = build_history_entry(
        attempt_number=2,
        guess=47,
        outcome="Too Low",
        message="Go HIGHER!",
        secret=50,
    )

    assert result == {
        "Attempt": 2,
        "Guess": 47,
        "Result": "Too Low",
        "Hint": "Go HIGHER!",
        "Distance": "Close",
    }


#FIX: Test that attempts is initialized to 0 after importing the app
def test_attempts_initial_zero():
    # Ensure a fresh import of the app module so top-level initialization runs
    if 'app' in sys.modules:
        del sys.modules['app']

    # Clear any prior session state
    st.session_state.clear()

    # Import app (this runs its top-level code which initializes session state)
    import app  # noqa: F401

    assert st.session_state.get('attempts') == 0


#FIX: Test that status is initialized to playing so the game is playable
def test_status_initial_playing():
    # Ensure a fresh import of the app module so top-level initialization runs
    if 'app' in sys.modules:
        del sys.modules['app']

    # Clear any prior session state
    st.session_state.clear()

    # Import app (this runs its top-level code which initializes session state)
    import app  # noqa: F401

    assert st.session_state.get('status') == "playing"


#FIX: Test that secret is within the difficulty range (Easy: 1-20)
def test_secret_in_easy_range():
    from logic_utils import get_range_for_difficulty
    low, high = get_range_for_difficulty("Easy")
    for _ in range(10):  # Test 10 times to account for randomness
        secret = random.randint(low, high)
        assert low <= secret <= high


#FIX: Test that secret is within the difficulty range (Hard: 1-50)
def test_secret_in_hard_range():
    from logic_utils import get_range_for_difficulty
    low, high = get_range_for_difficulty("Hard")
    for _ in range(10):  # Test 10 times to account for randomness
        secret = random.randint(low, high)
        assert low <= secret <= high

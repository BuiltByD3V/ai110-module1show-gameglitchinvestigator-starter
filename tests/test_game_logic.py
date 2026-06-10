import sys
import streamlit as st
from logic_utils import check_guess


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

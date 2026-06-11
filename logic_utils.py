def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            return False, None, "Please enter a whole number."

        value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def validate_guess_in_range(guess: int, low: int, high: int):
    """Return whether a guess is inside the active inclusive range."""
    if guess < low or guess > high:
        return False, f"Guess must be between {low} and {high}."

    return True, None


def describe_guess_distance(guess: int, secret: int):
    """Describe how close a guess was to the secret number."""
    distance = abs(guess - secret)

    if distance == 0:
        return "Exact"

    if distance <= 5:
        return "Close"

    if distance <= 15:
        return "Warm"

    return "Far"


def build_history_entry(attempt_number: int, guess: int, outcome: str, message: str, secret: int):
    """Build a display-ready row for the guess history table."""
    return {
        "Attempt": attempt_number,
        "Guess": guess,
        "Result": outcome,
        "Hint": message,
        "Distance": describe_guess_distance(guess, secret),
    }


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    
    #FIX: Moved here to fix the higher/lower bug - by centralizing the numeric comparison,
    # we avoid the app accidentally converting secret to a string, which flipped the hints.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

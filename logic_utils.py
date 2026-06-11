def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for a difficulty setting.

    Args:
        difficulty: The selected difficulty label from the Streamlit sidebar.

    Returns:
        A tuple containing the lowest and highest valid secret numbers.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Convert raw user input into a whole-number guess.

    Args:
        raw: The text entered by the player.

    Returns:
        A tuple of ``(ok, guess_int, error_message)``. ``ok`` is false when
        the input is blank, non-numeric, or not a whole number.
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
    """Check whether a guess is within the active difficulty range.

    Args:
        guess: The parsed whole-number guess.
        low: The lowest allowed value for the current round.
        high: The highest allowed value for the current round.

    Returns:
        A tuple of ``(is_valid, error_message)`` for UI-friendly validation.
    """
    if guess < low or guess > high:
        return False, f"Guess must be between {low} and {high}."

    return True, None


def describe_guess_distance(guess: int, secret: int):
    """Describe how close a guess is to the secret number.

    Args:
        guess: The player's valid guess.
        secret: The current round's secret number.

    Returns:
        A short label for display in the guess history table.
    """
    distance = abs(guess - secret)

    if distance == 0:
        return "Exact"

    if distance <= 5:
        return "Close"

    if distance <= 15:
        return "Warm"

    return "Far"


def build_history_entry(
    attempt_number: int,
    guess: int,
    outcome: str,
    message: str,
    secret: int,
):
    """Build a display-ready row for the guess history table.

    Args:
        attempt_number: The player's current attempt count.
        guess: The player's valid guess.
        outcome: The result returned by ``check_guess``.
        message: The hint message returned by ``check_guess``.
        secret: The current round's secret number.

    Returns:
        A dictionary whose keys become columns in Streamlit's history table.
    """
    return {
        "Attempt": attempt_number,
        "Guess": guess,
        "Result": outcome,
        "Hint": message,
        "Distance": describe_guess_distance(guess, secret),
    }


def check_guess(guess, secret):
    """Compare a player's guess with the secret number.

    Args:
        guess: The player's valid whole-number guess.
        secret: The current round's secret number.

    Returns:
        A tuple of ``(outcome, message)`` where outcome is ``"Win"``,
        ``"Too High"``, or ``"Too Low"``.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the score for a guess outcome.

    Args:
        current_score: The player's score before the current guess.
        outcome: The result of the current guess.
        attempt_number: The one-based attempt number for the current guess.

    Returns:
        The updated score.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )

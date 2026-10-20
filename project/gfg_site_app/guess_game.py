import random
# limit of 10 guesses, found as MAX_GUESS = 10 in views.py

def new_game():
    """Return a new special number."""
    return random.randint(1, 100)


def check_guess(raw_guess, special_number):
    """Return (status, message). Status is 'invalid', 'low', 'high' or 'correct'."""
    try:
        guess = int(float(raw_guess))
    except (ValueError, TypeError, OverflowError):
        return "invalid", "Invalid input. Please enter a number between 1 and 100."

    if not 1 <= guess <= 100:
        return "invalid", "Your guess must be between 1 and 100."
    if guess > special_number:
        return "high", f"{guess} is Too High"
    if guess < special_number:
        return "low", f"{guess} is Too Low"
    return "correct", "Correct!"
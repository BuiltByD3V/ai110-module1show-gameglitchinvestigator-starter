# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
   This project is a number guessing game where the player tries to guess a secret number within a limited number of attempts. The game provides feedback after each guess and allows the player to choose different difficulty levels that change the number range.
- [x] Detail which bugs you found.
   While testing the game, I noticed that changing the difficulty did not always update the secret number correctly. I also found that the higher/lower hints were sometimes wrong even when the guess was clearly above or below the secret number. In addition, the attempt counter started with the wrong value, and the New Game button did not fully reset the game after a win or loss.
- [x] Explain what fixes you applied.
   Using GitHub Copilot to help analyze the code, I traced the issues to the difficulty handling, guess comparison logic, and game state management. I updated the game so secret numbers are generated within the selected difficulty range, corrected the higher/lower hint logic by centralizing the comparison code, fixed the attempt counter initialization, and ensured the New Game button properly resets the game state. I also added tests to verify the fixes and reduce the chance of future regressions.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Choose a difficulty level from the sidebar and note the number range shown for that mode.
2. Enter your first guess in the input box and click Submit Guess.
3. Use the hint you get, then keep guessing until you narrow down the secret number.
4. Keep an eye on your attempts left and try to win before you run out.
5. When the round ends, click New Game to start a fresh round and play again with the same difficulty or a different one.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests\test_game_logic.py .................                                                                                                                                                   [100%]

======================================================================================= 17 passed in 0.35s ========================================================================================

```

## 🚀 Stretch Features

- [x] Challenge 4: Enhanced Game UI
  Added structured feedback in `app.py` so the game now shows a Current Status section with score, attempts left, and difficulty. The hint output is clearer for high and low guesses, and the game displays a Round Summary table with the selected difficulty, active range, attempts used, attempts remaining, score, and current status.

# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  When I first launched the application, it appeared to be a standard number-guessing game with a dark-themed interface. The page displayed the title "Game Glitch Investigator", a brief description, and a prompt asking the user to make a guess. The interface included the current number range (1–100), remaining attempts, a number input field, Submit Guess and New Game buttons, a Show Hint checkbox, and a collapsible Developer Debug Info section. A sidebar on the left allowed configuration of difficulty, number range, and maximum attempts.

- List at least two concrete bugs you noticed at the start  
  During testing, I identified several issues:

  1. Changing difficulty does not update range - Setting difficulty to Hard from Normal does not set the range to 1-50 for Hard and instead keeps it at the same range of 1-100 which is the range of Normal difficulty. The issue also exists for Easy difficulty which states a range of 1-20 but can generate a secret number outside of those restrictions.
  2. Incorrect higher/lower feedback – The game occasionally provides the wrong hint, telling the user to guess lower when the secret number is actually higher, and vice versa.
  3. Attempts counter starts with incorrect number - The counter start at -1 of the actual attempts and does not start to go down until the first two attempts are made.
  4. New Game does not fully reset end-state messages - After the game is won or lost, clicking New Game updates values like the secret number and attempts, but the previous end-state message ("You already won..." or "Game over...") still remains visible instead of clearing for a fresh round. The game is also no longer playable even though the UI resets the attempt counter and secret number.

  These issues affect both usability and gameplay accuracy.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 12 | "GO HIGHER!" | "GO LOWER!" | None |
| 36 | "GO LOWER" | "GO HIGHER" | None |
| Difficulty change to Hard | Secret number should only be between 1 and 50 | The secret number is able to generate outside of those restrictions | None |
| Click New Game after win/loss	| End-state message clears and game returns to clean state | Previous "You already won..." or "Game over..." message still displays after reset and game is unplayable | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used GitHub Copilot for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  A correct AI suggestion: centralize comparison logic into logic_utils.py so all hints come from one place. I accepted that refactor, updated app.py to import the helper, and wrote tests that assert the returned outcome/message tuples. The tests passed and the UI hints matched expected behavior.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  An incorrect AI suggestion: return string for higher/lower. After the AI implemented the fix for higher/lower hints, it mistakenly flipped the displayed strings. Example: "Too High! GO LOWER" string when the guess was actually higher than the secret and vice versa for the lower state.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was fixed by manually testing the functionality myself in streamlit and also running the test cases. Once the expected behavior was consistently reached across game testing and test casing, the bug was considered fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran pytest to verify the game logic and state fixes. One test checked that the secret number stays within the selected difficulty range, which confirmed that Easy, Normal, and Hard each generate valid secrets after the fix. I also tested that the attempts counter starts at 0 and that New Game resets the game back to a playable state.
- Did AI help you design or understand any tests? How?
  Yes, AI helped me design and understand the tests. It suggested splitting the game logic into logic_utils.py so the core behavior could be tested directly with pytest, and it also helped me think of regression tests for the range bug and the session state bugs. I verified the results by running the tests and checking that they passed.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns the whole app from top to bottom every time you interact with it, like clicking a button or changing a select box. Session state is how you keep values from disappearing between reruns, so things like the secret number, score, attempts, and game status stay available instead of resetting every time the script runs again.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
 One habit I want to reuse is writing tests before I assume a fix is done. This project showed me that even small state bugs can hide in Streamlit, so I want to keep separating logic into testable functions and verifying behavior with pytest instead of only relying on the UI. 
- What is one thing you would do differently next time you work with AI on a coding task?
  Next time, I would ask the AI for smaller, more focused pieces of help instead of letting it make broad changes all at once. That would make it easier for me to understand each fix and catch mistakes sooner. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project showed me that AI-generated code can be a helpful starting point, but it still needs careful review and testing. I learned that I should verify the logic myself and not assume the first version is correct.

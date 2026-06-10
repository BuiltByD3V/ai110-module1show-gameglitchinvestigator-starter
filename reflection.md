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
  4. New Game does not fully reset end-state messages - After the game is won or lost, clicking New Game updates values like the secret number and attempts, but the previous end-state message ("You already won..." or "Game over...") still remains visible instead of clearing for a fresh round.

  These issues affect both usability and gameplay accuracy.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 12 | "GO HIGHER!" | "GO LOWER!" | None |
| 36 | "GO LOWER" | "GO HIGHER" | None |
| Difficulty change to Hard | Secret number should only be between 1 and 50 | The secret number is able to generate outside of those restrictions | None |
| Click New Game after win/loss	| End-state message clears and game returns to clean state | Previous "You already won..." or "Game over..." message still displays after reset	| None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

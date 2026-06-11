# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Blank input | Help me identify edge cases that could break my number guessing game, then generate pytest tests for those cases. | `test_parse_guess_rejects_blank_input` | Yes | A blank guess should not crash the game or get treated like a real attempt at comparing numbers. |
| Text input | Generate a pytest case for a user typing a word instead of a number in my Streamlit guessing game. | `test_parse_guess_rejects_text_input` | Yes | The parser should return a friendly error instead of raising an exception. |
| Decimal input | Add a test for decimal guesses, since the game expects whole numbers only. | `test_parse_guess_rejects_decimal_input` | Yes | A decimal like `3.14` should not be silently converted to `3`, because that could confuse the player. |
| Negative number | Add a pytest case for guesses below the valid difficulty range. | `test_validate_guess_rejects_negative_number` | Yes | The active game range starts at 1, so negative guesses should be rejected with a clear range message. |
| Extremely large number | Add a pytest case for a guess far above the maximum valid number. | `test_validate_guess_rejects_extremely_large_number` | Yes | Very large guesses should not break the game or produce misleading higher/lower hints. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->

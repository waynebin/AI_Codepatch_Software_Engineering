# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
 When I first ran the game, it displayed a simple interface where I could input my guesses. However, I quickly noticed that the secret number kept changing every time I made a guess, which made it impossible to win the game. Additionally, the hints provided were not accurate; for example, if I guessed a number that was too low, the game would sometimes indicate that it was too high instead. These bugs made the game frustrating to play and highlighted the need for a stable secret number and correct hint logic.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
I used ChatGPT as my AI teammate for this project. One correct suggestion from ChatGPT was to use Streamlit's session state to store the secret number, which would prevent it from changing on every rerun. I implemented this suggestion and verified that the secret number remained consistent across guesses, allowing me to successfully play the game.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
To determine whether a bug was really fixed, I ran the game multiple times and made several guesses to see if the secret number remained consistent. For example, after implementing the session state fix, I guessed a number and then immediately guessed again to check if the secret number had changed. This manual testing showed that the secret number was now stable, confirming that the bug was fixed. AI helped me understand how to use Streamlit's session state effectively, which was crucial for designing the test to ensure the secret number did not change on reruns.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---
The secret number kept changing in the original app because Streamlit reruns the entire script every time a user interacts with the app (like making a guess). This means that any variable defined in the script, including the secret number, would be reinitialized on each interaction, leading to a new random number being generated every time. To explain Streamlit reruns and session state to a friend, I would say that Streamlit reruns the whole app whenever you interact with it, which can cause variables to reset. Session state is a way to store information across these reruns, allowing you to keep certain values (like the secret number) consistent throughout the user's interaction with the app. The change I made to give the game a stable secret number was to use Streamlit's session state to store the secret number, ensuring that it remained the same across all interactions until the user decides to reset it.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse in future projects is the practice of manually testing my code after implementing a fix, especially when working with AI-generated suggestions. This helps me ensure that the changes I made actually resolve the issue and that the game functions as intended. Next time I work with AI on a coding task, I would be more cautious about accepting suggestions without thoroughly understanding them first, as some AI suggestions can be incorrect or misleading. This project has made me realize that while AI can be a powerful tool for generating code and providing solutions, it's crucial to critically evaluate and test those suggestions rather than relying on them blindly.

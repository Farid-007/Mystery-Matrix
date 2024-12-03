# app.py
from flask import Flask, request, render_template
import random
from flask_cors import CORS  # Optional, for CORS support

app = Flask(__name__)
CORS(app)  # Enable CORS if needed

# Game variables
lowest = 1
highest = 10
answer = random.randint(lowest, highest)
guesses = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global guesses, answer
    feedback = ""
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            guesses += 1
            if guess < answer:
                feedback = "Too low! Try again."
            elif guess > answer:
                feedback = "Too high! Try again."
            else:
                feedback = f"🎉 Correct! You guessed it in {guesses} tries."
                # Reset the game
                answer = random.randint(lowest, highest)
                guesses = 0
        except ValueError:
            feedback = "⚠️ Please enter a valid number."
    return render_template("index.html", feedback=feedback, lowest=lowest, highest=highest)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

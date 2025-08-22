import random

# List of words and their meanings (word: [correct_answer, wrong1, wrong2])
vocabulary = {
    "benevolent": ["kind and generous", "angry and rude", "lazy and slow"],
    "elated": ["very happy", "confused", "bored"],
    "brisk": ["quick and energetic", "sad and lonely", "tired and weak"],
    "vivid": ["bright and clear", "dull and boring", "small and weak"],
    "timid": ["shy and nervous", "brave and bold", "fast and wild"]
}

score = 0
rounds = 3

print("🎓 Welcome to the Word Guessing Game!\nGuess the meaning of the word.\n")

# Pick random words for the number of rounds
words = random.sample(list(vocabulary.keys()), rounds)

for i, word in enumerate(words, 1):
    print(f"\n🔤 Round {i}: What does '{word}' mean?")

    # Get and shuffle options
    options = vocabulary[word]
    correct_answer = options[0]
    random.shuffle(options)

    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    # Get user input
    try:
        choice = int(input("Your choice (1-3): "))
        if options[choice - 1] == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was: {correct_answer}")
    except (ValueError, IndexError):
        print(f"⚠️ Invalid input. The correct answer was: {correct_answer}")

print(f"\n🎉 Game Over! Your score: {score}/{rounds}")

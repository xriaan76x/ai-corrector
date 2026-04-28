from textblob import TextBlob

common_words = {
    "gud": "good",
    "englih": "english",
    "u": "you",
    "ur": "your",
    "pls": "please",
    "thx": "thanks",
    "becoz": "because",
    "frnd": "friend",
    "luv": "love",
    "msg": "message",
    "abt": "about"
}

def correct_text(text):
    words = text.split()
    fixed = []

    for word in words:
        clean = word.lower().strip(".,!?")

        if clean in common_words:
            new_word = common_words[clean]
        else:
            new_word = str(TextBlob(word).correct())

        fixed.append(new_word)

    return " ".join(fixed)

def get_suggestions(text):
    original = text.split()
    corrected = correct_text(text).split()

    suggestions = []

    for i in range(min(len(original), len(corrected))):
        if original[i] != corrected[i]:
            suggestions.append({
                "error": original[i],
                "suggestions": corrected[i]
            })

    return suggestions

def grammar_score(text):
    corrected = correct_text(text)

    if text.strip() == "":
        return 0

    same = 0
    original_words = text.split()
    corrected_words = corrected.split()

    for i in range(min(len(original_words), len(corrected_words))):
        if original_words[i].lower() == corrected_words[i].lower():
            same += 1

    score = int((same / len(original_words)) * 100)
    return score
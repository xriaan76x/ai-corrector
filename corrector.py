from textblob import TextBlob

def correct_text(text):
    return str(TextBlob(text).correct())

def get_suggestions(text):
    original = text.split()
    corrected = str(TextBlob(text).correct()).split()

    suggestions = []

    for i in range(min(len(original), len(corrected))):
        if original[i] != corrected[i]:
            suggestions.append({
                "error": original[i],
                "suggestions": corrected[i]
            })

    return suggestions
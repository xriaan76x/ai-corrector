import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def correct_text(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text


def get_suggestions(text):
    matches = tool.check(text)
    suggestions = []

    for match in matches:
        suggestions.append({
            "error": text[match.offset : match.offset + match.error_length],
            "suggestions": match.replacements
        })

    return suggestions
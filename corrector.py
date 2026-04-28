import re
from textblob import TextBlob

common_words = {
    "u":"you","ur":"your","urs":"yours","r":"are","n":"and",
    "pls":"please","pls":"please","plzz":"please","thx":"thanks","thanx":"thanks",
    "gud":"good","goood":"good","guddd":"good","nicee":"nice","nyc":"nice",
    "helo":"hello","helloo":"hello","hii":"hi","hiii":"hi","byee":"bye",
    "englih":"english","englsh":"english","langauge":"language",
    "frnd":"friend","frnds":"friends","broo":"bro","brooo":"bro",
    "luv":"love","lv":"love","msg":"message","msging":"messaging",
    "abt":"about","becoz":"because","bcoz":"because","coz":"because",
    "tmrw":"tomorrow","nite":"night","tonite":"tonight",
    "hav":"have","hv":"have","wer":"were","wen":"when","wat":"what",
    "wht":"what","whr":"where","y":"why","c":"see",
    "im":"I am","ive":"I have","ill":"I will","idk":"I do not know",
    "dont":"don't","cant":"can't","wont":"won't","didnt":"didn't",
    "isnt":"isn't","arent":"aren't","wasnt":"wasn't","werent":"weren't",
    "shud":"should","shld":"should","wud":"would","clg":"college",
    "msged":"messaged","alot":"a lot","smth":"something",
    "btw":"by the way","bc":"because","fav":"favorite"
}

grammar_fixes = {
    "i is":"I am",
    "i has":"I have",
    "i goes":"I go",
    "he go":"he goes",
    "she go":"she goes",
    "they is":"they are",
    "we is":"we are",
    "you is":"you are"
}

def reduce_letters(word):
    return re.sub(r'(.)\1{2,}', r'\1', word)

def fix_word(word):
    if not word:
        return word

    lw = word.lower()

    if lw in common_words:
        return common_words[lw]

    lw = reduce_letters(lw)

    if lw in common_words:
        return common_words[lw]

    corrected = str(TextBlob(lw).correct())

    if corrected in common_words:
        corrected = common_words[corrected]

    return corrected

def capitalize_i(text):
    words = text.split()
    final = []

    for w in words:
        if w.lower() == "i":
            final.append("I")
        else:
            final.append(w)

    return " ".join(final)

def apply_grammar(text):
    lower_text = text.lower()

    for wrong, right in grammar_fixes.items():
        lower_text = lower_text.replace(wrong, right.lower())

    return lower_text

def sentence_case(text):
    if not text:
        return text

    text = text.strip()
    return text[0].upper() + text[1:]

def punctuation_fix(text):
    text = re.sub(r"\s+([,.!?])", r"\1", text)

    if text and text[-1] not in ".!?":
        text += "."

    return text

def correct_text(text):
    words = text.split()
    fixed_words = []

    for word in words:
        punct = ""

        if len(word) > 0 and word[-1] in ".,!?":
            punct = word[-1]
            word = word[:-1]

        new_word = fix_word(word)
        fixed_words.append(new_word + punct)

    sentence = " ".join(fixed_words)
    sentence = apply_grammar(sentence)
    sentence = capitalize_i(sentence)
    sentence = sentence_case(sentence)
    sentence = punctuation_fix(sentence)

    return sentence

def get_suggestions(text):
    original = text.split()
    corrected = correct_text(text).replace(".", "").split()

    suggestions = []

    for i in range(min(len(original), len(corrected))):
        if original[i].lower() != corrected[i].lower():
            suggestions.append({
                "error": original[i],
                "suggestions": corrected[i]
            })

    return suggestions

def grammar_score(text):
    if not text.strip():
        return 0

    original = text.lower().replace(".", "").split()
    corrected = correct_text(text).lower().replace(".", "").split()

    same = 0

    for i in range(min(len(original), len(corrected))):
        if original[i] == corrected[i]:
            same += 1

    score = int((same / len(original)) * 100)
    return score
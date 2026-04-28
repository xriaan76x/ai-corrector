import re
from textblob import TextBlob

# Main dictionary
common_words = {
    "u":"you","ur":"your","urs":"yours","r":"are","n":"and",
    "pls":"please","plz":"please","plzz":"please","plsss":"please",
    "thx":"thanks","thanx":"thanks","ty":"thank you","tysm":"thank you so much",
    "yw":"you're welcome","wc":"welcome",

    "helo":"hello","helloo":"hello","heloo":"hello","hellooo":"hello",
    "hii":"hi","hiii":"hi","hiiii":"hi",
    "gm":"good morning","gn":"good night","ge":"good evening",

    "gud":"good","goood":"good","guddd":"good","gooooood":"good",
    "nicee":"nice","nyc":"nice","gr8":"great","awsm":"awesome",
    "oky":"okay","okk":"okay","okkk":"okay","acha":"okay","accha":"okay",

    "msg":"message","msging":"messaging","txt":"text",
    "abt":"about","bcoz":"because","becoz":"because","coz":"because",
    "tmrw":"tomorrow","tmr":"tomorrow","nite":"night","tonite":"tonight",
    "frnd":"friend","frnds":"friends","frn":"friend",
    "broo":"bro","brooo":"bro",

    "luv":"love","lv":"love","lyk":"like","liek":"like",
    "wanna":"want to","gonna":"going to","gotta":"got to",

    "im":"I am","ive":"I have","ill":"I will","idk":"I do not know",
    "dont":"don't","cant":"can't","wont":"won't","didnt":"didn't",
    "isnt":"isn't","arent":"aren't","wasnt":"wasn't","werent":"weren't",
    "hav":"have","hv":"have",

    "wat":"what","wht":"what","whr":"where","wen":"when","hw":"how",

    "englih":"english","englsh":"english","langauge":"language",
    "recieve":"receive","definately":"definitely","seperate":"separate",
    "wierd":"weird","becuase":"because","adress":"address",
    "freind":"friend","beleive":"believe","acheive":"achieve",
    "alot":"a lot","somthing":"something","smth":"something",

    "kr":"do","kro":"do","krna":"do","mt":"don't",
    "hn":"yes","haan":"yes","ha":"yes",
    "nhi":"no","nahi":"no",
    "jaldi":"quickly","thik":"okay","theek":"okay",

    "fav":"favorite","btw":"by the way","fyi":"for your information"
}

# Smart phrases
smart_phrases = {
    "wru":"where are you",
    "wyd":"what are you doing",
    "hru":"how are you",
    "im fine":"I am fine",
    "cya":"see you",
    "brb":"be right back",
    "gtg":"got to go",
    "omw":"on my way",
    "idc":"I don't care",
    "ikr":"I know right",
    "nvm":"never mind",
    "tbh":"to be honest",
    "ily":"I love you",
    "lmk":"let me know",
    "asap":"as soon as possible",
    "ttyl":"talk to you later",
    "np":"no problem",
    "dw":"don't worry",
    "miss u":"miss you",
    "love u":"love you",
    "see u":"see you"
}

# Phrase fixes
phrase_fixes = {
    "how r u":"how are you",
    "where r u":"where are you",
    "what r u doing":"what are you doing",
    "thank u":"thank you",
    "can u help me":"can you help me",
    "u r amazing":"you are amazing"
}

def reduce_letters(word):
    return re.sub(r'(.)\1{2,}', r'\1', word)

def fix_word(word):
    if not word:
        return word

    low = word.lower().strip()

    if low in common_words:
        return common_words[low]

    low = reduce_letters(low)

    if low in common_words:
        return common_words[low]

    corrected = str(TextBlob(low).correct())

    if corrected in common_words:
        corrected = common_words[corrected]

    return corrected
# Grammar rules
grammar_fixes = {
    "i is":"I am",
    "i has":"I have",
    "you is":"you are",
    "we is":"we are",
    "they is":"they are",
    "he go":"he goes",
    "she go":"she goes",
    "he have":"he has",
    "she have":"she has",
    "they was":"they were",
    "we was":"we were"
}

# Context rules
context_rules = {
    "a apple":"an apple",
    "a orange":"an orange",
    "a egg":"an egg",
    "a umbrella":"an umbrella",
    "an dog":"a dog",
    "an cat":"a cat",
    "an book":"a book",
    "there is many":"there are many",
    "there is people":"there are people",
    "me is":"I am",
    "me have":"I have"
}

def apply_smart_phrases(text):
    low = text.lower()

    for wrong, right in smart_phrases.items():
        low = low.replace(wrong, right.lower())

    return low

def apply_phrase_fixes(text):
    low = text.lower()

    for wrong, right in phrase_fixes.items():
        low = low.replace(wrong, right.lower())

    return low

def apply_grammar(text):
    low = text.lower()

    for wrong, right in grammar_fixes.items():
        low = low.replace(wrong, right.lower())

    return low

def apply_context_rules(text):
    low = text.lower()

    for wrong, right in context_rules.items():
        low = low.replace(wrong, right.lower())

    return low

def capitalize_i(text):
    words = text.split()
    final = []

    for w in words:
        if w.lower() == "i":
            final.append("I")
        else:
            final.append(w)

    return " ".join(final)

def sentence_case(text):
    if not text:
        return text

    text = text.strip()
    return text[:1].upper() + text[1:]

def punctuation_fix(text):
    text = re.sub(r"\s+([,.!?])", r"\1", text)

    if text and text[-1] not in ".!?":
        text += "."

    return text
def correct_text(text):
    if not text.strip():
        return ""

    text = apply_smart_phrases(text)
    text = apply_phrase_fixes(text)

    words = text.split()
    fixed_words = []

    for word in words:
        punctuation = ""

        if len(word) > 0 and word[-1] in ".,!?":
            punctuation = word[-1]
            word = word[:-1]

        new_word = fix_word(word)

        if new_word.lower() == "i":
            new_word = "I"

        fixed_words.append(new_word + punctuation)

    sentence = " ".join(fixed_words)

    sentence = apply_grammar(sentence)
    sentence = apply_context_rules(sentence)
    sentence = capitalize_i(sentence)
    sentence = sentence_case(sentence)
    sentence = punctuation_fix(sentence)

    return sentence


def get_suggestions(text):
    if not text.strip():
        return []

    original = text.replace(".", "").replace(",", "").split()
    corrected = correct_text(text).replace(".", "").replace(",", "").split()

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

    original = (
        text.lower()
        .replace(".", "")
        .replace(",", "")
        .replace("!", "")
        .replace("?", "")
        .split()
    )

    corrected = (
        correct_text(text)
        .lower()
        .replace(".", "")
        .replace(",", "")
        .replace("!", "")
        .replace("?", "")
        .split()
    )

    if len(original) == 0:
        return 0

    same = 0

    for i in range(min(len(original), len(corrected))):
        if original[i] == corrected[i]:
            same += 1

    score = int((same / len(original)) * 100)

    if score > 100:
        score = 100

    return score
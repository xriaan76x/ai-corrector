import re
from textblob import TextBlob

common_words = {
    # basic chat
    "u":"you","ur":"your","urs":"yours","r":"are","n":"and",
    "pls":"please","plz":"please","plzz":"please","plsss":"please",
    "thx":"thanks","thanx":"thanks","ty":"thank you","tysm":"thank you so much",
    "yw":"you're welcome","wc":"welcome",

    # greetings
    "helo":"hello","helloo":"hello","heloo":"hello","hellooo":"hello",
    "hii":"hi","hiii":"hi","hiiii":"hi",
    "gm":"good morning","gn":"good night","ge":"good evening",

    # common words
    "gud":"good","goood":"good","guddd":"good","gooooood":"good",
    "nicee":"nice","nyc":"nice","gr8":"great","awsm":"awesome",
    "oky":"okay","okk":"okay","okkk":"okay","acha":"okay",
    "bt":"but","buttt":"but",

    # texting
    "msg":"message","msging":"messaging","txt":"text",
    "abt":"about","bcoz":"because","becoz":"because","coz":"because",
    "tmrw":"tomorrow","tmr":"tomorrow","nite":"night","tonite":"tonight",
    "frnd":"friend","frnds":"friends","frn":"friend",
    "broo":"bro","brooo":"bro","sisoo":"sis",

    # feelings / actions
    "luv":"love","lv":"love","lyk":"like","liek":"like",
    "wanna":"want to","gonna":"going to","gotta":"got to",
    "cud":"could","shud":"should","wud":"would",

    # grammar helpers
    "im":"I am","ive":"I have","ill":"I will","idk":"I do not know",
    "dont":"don't","cant":"can't","wont":"won't","didnt":"didn't",
    "isnt":"isn't","arent":"aren't","wasnt":"wasn't","werent":"weren't",
    "doesnt":"doesn't","hav":"have","hv":"have","hadnt":"hadn't",

    # question words
    "wat":"what","wht":"what","whr":"where","wen":"when",
    "y":"why","hw":"how","whn":"when",

    # college / casual
    "clg":"college","uni":"university","subj":"subject",
    "hw":"homework","proj":"project","assgn":"assignment",

    # typo fixes
    "englih":"english","englsh":"english","langauge":"language",
    "recieve":"receive","definately":"definitely","seperate":"separate",
    "wierd":"weird","becuase":"because","adress":"address",
    "occured":"occurred","untill":"until","tommorow":"tomorrow",
    "freind":"friend","beleive":"believe","acheive":"achieve",
    "enviroment":"environment","goverment":"government",
    "succes":"success","succesful":"successful","sucess":"success",
    "alot":"a lot","somthing":"something","smth":"something",
    "everytime":"every time","infact":"in fact",

    # Hinglish / Indian texting
    "kr":"do","kro":"do","krna":"do","krne":"doing",
    "mt":"don't","hn":"yes","haan":"yes","ha":"yes",
    "nhi":"no","nahi":"no","acha":"okay","accha":"okay",
    "jaldi":"quickly","thik":"okay","theek":"okay",

    # misc
    "fav":"favorite","asap":"as soon as possible",
    "imo":"in my opinion","irl":"in real life",
    "btw":"by the way","fyi":"for your information"
}

phrase_fixes = {
    "how r u":"how are you",
    "where r u":"where are you",
    "what r u doing":"what are you doing",
    "i cant":"I can't",
    "i dont":"I don't",
    "i wont":"I won't",
    "thank u":"thank you",
    "love u":"love you",
    "miss u":"miss you",
    "see u":"see you",
    "good nite":"good night",
    "good mrng":"good morning",
    "hows u":"how are you"
}

grammar_fixes = {
    "i is":"I am",
    "i has":"I have",
    "you is":"you are",
    "we is":"we are",
    "they is":"they are",
    "he go":"he goes",
    "she go":"she goes",
    "he have":"he has",
    "she have":"she has"
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
# --- More dictionary entries ---
common_words.update({
    # more chat
    "brotherr":"brother","sistr":"sister","fam":"family",
    "bday":"birthday","congo":"congratulations","congrats":"congratulations",
    "gd":"good","vry":"very","verry":"very","soo":"so","sooo":"so",
    "realy":"really","rlly":"really","tru":"true","fals":"false",

    # verbs
    "comin":"coming","goin":"going","doin":"doing","makin":"making",
    "sayin":"saying","tellin":"telling","givin":"giving",
    "takin":"taking","talkin":"talking","thinkin":"thinking",

    # daily words
    "wrk":"work","wrkng":"working","studing":"studying",
    "studin":"studying","examz":"exams","lect":"lecture",
    "prblm":"problem","soln":"solution","ques":"question",
    "ans":"answer","imp":"important",

    # places / time
    "tm":"time","tym":"time","mins":"minutes","sec":"seconds",
    "hrs":"hours","wk":"week","mnth":"month",

    # feelings
    "happpy":"happy","hapy":"happy","sadd":"sad",
    "angryy":"angry","tirdd":"tired","exited":"excited",
    "borred":"bored","lonley":"lonely",

    # mistakes
    "tommorow":"tomorrow","agian":"again","agianst":"against",
    "agiann":"again","wierd":"weird","wierdly":"weirdly",
    "becouse":"because","becasue":"because","becuase":"because",
    "definately":"definitely","definetly":"definitely",
    "seperately":"separately","untill":"until",
    "finaly":"finally","basicly":"basically",
    "accomodate":"accommodate","acommodate":"accommodate",
    "begining":"beginning","calender":"calendar",
    "cemetry":"cemetery","comming":"coming",
    "embarass":"embarrass","foriegn":"foreign",
    "guage":"gauge","happend":"happened",
    "immediatly":"immediately","knowlege":"knowledge",
    "liason":"liaison","maintainance":"maintenance",
    "neccessary":"necessary","occassion":"occasion",
    "publically":"publicly","reccommend":"recommend",
    "tounge":"tongue","untill":"until",
    "vaccum":"vacuum","writting":"writing"
})

phrase_fixes.update({
    "where u at":"where are you",
    "what u doing":"what are you doing",
    "how u doing":"how are you doing",
    "i miss u":"I miss you",
    "i luv u":"I love you",
    "can u help me":"can you help me",
    "will u come":"will you come",
    "are u okay":"are you okay",
    "u are amazing":"you are amazing",
    "u r amazing":"you are amazing",
    "good job bro":"good job bro",
    "pls help":"please help",
    "plz help":"please help",
    "thx bro":"thanks bro",
    "thank u so much":"thank you so much",
    "see u soon":"see you soon",
    "miss u bro":"miss you bro"
})

grammar_fixes.update({
    "this are":"this is",
    "these is":"these are",
    "there is many":"there are many",
    "me and him was":"he and I were",
    "me and her was":"she and I were",
    "i done":"I did",
    "i seen":"I saw",
    "he don't":"he doesn't",
    "she don't":"she doesn't",
    "it don't":"it doesn't",
    "they doesn't":"they don't"
})

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

    # phrase-level cleanup first
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

    # grammar-level cleanup
    sentence = apply_grammar(sentence)

    # capitalize standalone I
    sentence = capitalize_i(sentence)

    # first letter uppercase
    sentence = sentence_case(sentence)

    # punctuation
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

    # cap at 100
    if score > 100:
        score = 100

    return score
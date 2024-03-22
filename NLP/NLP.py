import liwc
import unicodedata

parse, category_names = liwc.load_token_parser("./LIWC2007_Portugues_win.dic")

file = open("demofile.txt", "r", encoding="utf8")
text_original = file.read()

file2 = open("demofile2.txt", "r", encoding="utf8")
text_original2 = file2.read()

def remove_non_ascii_normalized(text):
    normalized = unicodedata.normalize('NFD', text)
    return normalized.encode('ascii', 'ignore').decode('utf-8')

def text_cleaning(text):
    for char in text:
        if char == ".":
            text = text.replace(char, "  ")
        elif char == ",":
            text = text.replace(char, "  ")
        elif char == ";":  
            text = text.replace(char, "  ")
        elif char == ":": 
            text = text.replace(char, "  ")
        elif char == "(":
            text = text.replace(char, "  ")
        elif char == ")":
            text = text.replace(char, "  ")
        elif char == "[":
            text = text.replace(char, "  ")
        elif char == "]":
            text = text.replace(char, "  ")
        elif char == "{":
            text = text.replace(char, "  ")
        elif char == "}":
            text = text.replace(char, "  ")
        elif char == '"':
            text = text.replace(char, "  ")
        elif char == "'":
            text = text.replace(char, "  ")
        elif char == "!":
            text = text.replace(char, "  ")
        elif char == "?":
            text = text.replace(char, "  ")
        elif char == "-":
            text = text.replace(char, "  ")
        elif char == "_":
            text = text.replace(char, "  ")
        elif char == "+":
            text = text.replace(char, "  ")
        elif char == "=":
            text = text.replace(char, "  ")
        elif char == "*":
            text = text.replace(char, "  ")
        elif char == "/":
            text = text.replace(char, "  ")
        elif char == "\\":
            text = text.replace(char, "  ")
        elif char == "|":
            text = text.replace(char, "  ")
        elif char == "@":
            text = text.replace(char, "  ")
        elif char == "#":
            text = text.replace(char, "  ")
        elif char == "$":
            text = text.replace(char, "  ")
        elif char == "%":
            text = text.replace(char, "  ")
        elif char == "&":
            text = text.replace(char, "  ")
        elif char == "^":
            text = text.replace(char, "  ")
        elif char == "~":
            text = text.replace(char, "  ")
        elif char == "`":
            text = text.replace(char, "  ")
        elif char == "<":
            text = text.replace(char, "  ")
        elif char == ">":
            text = text.replace(char, "  ")
        elif char == "´":
            text = text.replace(char, "  ")
        elif char == "¨":
            text = text.replace(char, "  ")
        elif char == "ª":
            text = text.replace(char, "  ")
        elif char == "º":
            text = text.replace(char, "  ")
    return text

def text_lowercasing(text):
    text = text.lower()
    return text

def text_tokenization(text):
    text = text.split()
    return text

def text_liwc(text):
    res = []
    for word in text:
        resp = list(parse(word))
        res.append(resp)
    return res

def swear_count(res):
    count = 0
    for word in res:
        for type in word:
            if type == 'swear':
                count += 1
    return count

def anx_count(res):
    count = 0
    for word in res:
        for type in word:
            if type == 'anx':
                count += 1
    return count

def posemo_count(res):
    count = 0
    for word in res:
        for type in word:
            if type == 'posemo':
                count += 1
    percentage = (count/len(res)) * 100
    return percentage

def negemo_count(res):
    count = 0
    for word in res:
        for type in word:
            if type == 'negemo':
                count += 1
    percentage = (count/len(res)) * 100
    return percentage

def text_sentiment(text_original):
    text = remove_non_ascii_normalized(text_original)
    text = text_cleaning(text)
    text = text_lowercasing(text)   
    text = text_tokenization(text)
    res = text_liwc(text)

    print('Quantidade de palavras:', len(res))
    print('Quantidade de palavras ofensivas:', swear_count(res))
    print('Quantidade de palavras ansiosas: ', anx_count(res))
    print(f'Tom geral positivo: {posemo_count(res):.2f} %')
    print(f'Tom geral negativo: {negemo_count(res):.2f} %')

text_sentiment(text_original)
text_sentiment(text_original2)
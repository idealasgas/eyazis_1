import nltk
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
from collections import defaultdict
nltk.download('punkt')

#Create lemmatizer and stopwords list
mystem = Mystem()
russian_stopwords = stopwords.words("russian")
not_words = [',', '.', '!', '?']

#Preprocess function
def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords\
              and token != " " \
              and token.strip() not in punctuation]
    return tokens
    # text = " ".join(tokens)


def forms_of_words(text):
  forms = defaultdict(lambda: 0)
  tokens = nltk.word_tokenize(text)
  for token in tokens:
    if not token in not_words:
      forms[token] += 1
  # print(forms)

def lexems(text):
  tokens = preprocess_text(text)
  lexems = defaultdict(lambda: 0)
  for token in tokens:
    if not token in not_words:
      lexems[token] += 1
  # print(lexems)

preprocess_text("Ворон к ворону летит. Ворон ворону кричит: Ворон! Где б нам отобедать?")
forms_of_words('Я очень люблю кушать, но сейчас не кушаю а вот кушала бы и кушала бы')
lexems('Я очень люблю кушать, но сейчас не кушаю а вот кушала бы и кушала бы')
# import tkinter
# tkinter._test()

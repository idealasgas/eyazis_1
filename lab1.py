import nltk
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
from collections import defaultdict
nltk.download('punkt')
from tkinter import ttk
import tkinter as tk
from tkinter import *

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
  return forms

def get_lexems(text):
  tokens = preprocess_text(text)
  lexems = defaultdict(lambda: 0)
  for token in tokens:
    if not token in not_words:
      lexems[token] += 1
  return lexems

# preprocess_text("Ворон к ворону летит. Ворон ворону кричит: Ворон! Где б нам отобедать?")
# forms_of_words('Я очень люблю кушать, но сейчас не кушаю а вот кушала бы и кушала бы')
# lexems('Я очень люблю кушать, но сейчас не кушаю а вот кушала бы и кушала бы')

def process_text():
  input = text.get(1.0, END)
  forms = forms_of_words(input)
  lexems = get_lexems(input)
  for key, value in forms.items():
    tree.insert("", "end", text="%s" % key, values=('%s' % value))
  print(forms)
  print(lexems)


def OnDoubleClick(event):
  item = tree.selection()
  print('item:', item)
  print('event:', event)
  item = tree.selection()[0]
  print("you clicked on", tree.item(item,"text"))

root = tk.Tk()

text = Text(width=25, height=5)
text.pack()

frame = Frame()
frame.pack()

button = Button(frame, text="Обработать", command=process_text)
button.pack(side=LEFT)

tree = ttk.Treeview()
tree.pack()

tree["columns"]=("one","two","three")

tree.heading("#0",text="Forms",anchor=tk.W)
tree.heading("one", text="Count",anchor=tk.W)

# for i in range(10):
#   tree.insert("", "end", text="Item %s" % i)

tree.bind("<<TreeviewSelect>>", OnDoubleClick)

root.mainloop()

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
vocabulary = {}

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
  tokens.sort()
  for token in tokens:
    if not token in not_words:
      forms[token] += 1

  for form in forms:
    count = forms[form]
    forms[form] = [count, '']
  return forms

def get_lexems(text):
  tokens = preprocess_text(text)
  tokens.sort()
  lexems = defaultdict(lambda: 0)
  for token in tokens:
    if not token in not_words:
      lexems[token] += 1
  return lexems

def process_text():
  input = text.get(1.0, END)
  forms = forms_of_words(input)
  lexems = get_lexems(input)
  vocabulary['forms'] = forms
  vocabulary['lexems'] = lexems
  for key, value in forms.items():
    tree.insert("", "end", text="%s" % key, values=('%s' % value[0], value[1]))
  for key, value in lexems.items():
    lexems_tree.insert("", "end", text="%s" % key, values=('%s' % value))

def add_note():
  text_field.pack()
  submit_button.pack()

def submit():
  notes = text_field.get(1.0, END)
  text_field.pack_forget()
  submit_button.pack_forget()

  item = tree.selection()
  value = tree.item(item)['values'][0]
  text = tree.item(item)['text']
  vocabulary['forms'][text][1] = notes
  tree.item(item, values=(value, notes))
  print(vocabulary)

def save_vocabulary():
  print('hello')

def upload_vocabulary():
  print('rocketship')

root = tk.Tk()

text = Text(width=25, height=5)
text.pack()

text_field = Text(width=25, height=5)
submit_button = Button(text='Добавить', command=submit)

frame = Frame()
frame.pack()

button = Button(frame, text="Обработать", command=process_text)
button.pack(side=LEFT)

tree = ttk.Treeview()
tree.pack()

lexems_tree = ttk.Treeview()
lexems_tree.pack()

lexems_tree["columns"]=("one","two")

lexems_tree.heading("#0",text="Lexems",anchor=tk.W)
lexems_tree.heading("one", text="Count",anchor=tk.W)

add_note_button = Button(frame, text='Add note', command=add_note)
add_note_button.pack()

save_vocabulary_button = Button(frame, text='Save to file', command=save_vocabulary)
save_vocabulary_button.pack()

upload_from_file_button = Button(frame, text='Upload from file', command=upload_vocabulary)
upload_from_file_button.pack()

tree["columns"]=("one","two")

tree.heading("#0",text="Forms",anchor=tk.W)
tree.heading("one", text="Count",anchor=tk.W)
tree.heading("two", text="Notes",anchor=tk.W)

root.mainloop()

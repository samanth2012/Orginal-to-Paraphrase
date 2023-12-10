from django.shortcuts import render
from django.http import HttpResponse
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import numpy as np
from tensorflow.python.keras.optimizer_v2 import adam

import sqlite3
import mysql.connector
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn


def hello(request):
    return HttpResponse("Hello")




def home(request):
    return render(request, 'home.html')

# Define the paraphrasing functions
def tag(sentence):
    words = word_tokenize(sentence)
    words = pos_tag(words)
    return words

def paraphraseable(tag):
    return tag.startswith('NN') or tag.startswith('VB') or tag.startswith('JJ') or tag.startswith('RB')

def pos(tag):
    if tag.startswith('NN'):
        return wn.NOUN
    elif tag.startswith('V'):
        return wn.VERB
    elif tag.startswith('JJ'):
        return wn.ADJ
    elif tag.startswith('RB'):
        return wn.ADV
    else:
        return None

def synonyms(word, tag):
    pos_value = pos(tag)
    if pos_value:
        lemma_lists = [ss.lemmas() for ss in wn.synsets(word, pos_value)]
        lemmas = [lemma.name() for lemma in sum(lemma_lists, [])]
        return set(lemmas)
    return set()

def synonymIfExists(sentence):
    paraphrased_sentence = []
    for (word, t) in tag(sentence):
        if paraphraseable(t):
            syns = synonyms(word, t)
            if syns:
                paraphrased_sentence.append(list(syns)[0])  # Use the first synonym for simplicity
                continue
        paraphrased_sentence.append(word)
    return ' '.join(paraphrased_sentence)



def sentimentanalasis(request):
     if request.method == 'POST':
        val1 = request.POST.get('num1') 
        original_sentence =val1
        paraphrased_sentence = synonymIfExists(original_sentence)

#Initialize the database by filling details of sql user credentials and database name
        mydb = mysql.connector.connect(
  host ="192.168.55.103",
  user ="Samanth",
  passwd ="Samanth12@",
  database="movies"
)
 #Here we find the prediction of sentiment and insert the predicition into sql database
        sequences = Tokenizer().texts_to_sequences(val1)
        test = pad_sequences(sequences, maxlen=500)
        custom_optimizer = adam.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-7, amsgrad=False)

        loaded_model = load_model('moviereviews12.h5', custom_objects={'Adam': custom_optimizer}, compile=False)
        res=loaded_model.predict(test)
        pred=res[0]
        
            
        mycursor = mydb.cursor()
        sql_insert_data = "INSERT INTO paraphrase_data (original_text, paraphrased_text) VALUES (%s, %s)"

# Execute the SQL statement with the data
        mycursor.execute(sql_insert_data, (original_sentence, paraphrased_sentence,))




        mydb.commit()

        mycursor.close()
        mydb.close()


    
        return render(request, "result.html", {'result': paraphrased_sentence,'state': val1,'re1':pred})
     

     else:

        return HttpResponse("Method Not Allowed", status=405)
    

 
  



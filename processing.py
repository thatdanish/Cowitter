from tensorflow.keras.models import load_model
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from nltk.tokenize import word_tokenize


len_max = 94
lemma = WordNetLemmatizer()

def call_model():
    model = load_model("Model/Final_Model")   #calls model
    return model

def prep_input(sent):
    final_input = []
    sent = sent.lower()           #prepares input for proper prediction
    clean_sent = sent.translate(str.maketrans('','',string.punctuation))
    words = word_tokenize(sent)
    clean_words = [k for k in words if k not in stopwords.words('english')]
    lemma_words = [lemma.lemmatize(i) for i in clean_words]

    final_input.append(lemma_words)

    return final_input
    

def preprocess_data(data):
    final_input = prep_input(data)
    unique_words = len(final_input)
    tokenizer = Tokenizer(num_words = unique_words)
    tokenizer.fit_on_texts(final_input)                        #prepares data for final prediction
    final_input = tokenizer.texts_to_sequences(final_input)
    final_input = sequence.pad_sequences(final_input,maxlen=len_max)

    return final_input

    
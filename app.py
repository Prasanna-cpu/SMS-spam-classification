import streamlit as st
import pickle
from spacy import load
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.cli import download
download("en_core_web_sm")

nlp = load("en_core_web_sm")

def transform(text):
    text = text.lower()
    doc = nlp(text)
    tokens = [token.text for token in doc if token.is_alpha]
    tokens = [token for token in tokens if token not in STOP_WORDS and token not in string.punctuation]
    lemmatized_tokens = [token.lemma_ for token in nlp(" ".join(tokens))]
    return " ".join(lemmatized_tokens)
            

tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title("SMS SPAM CLASSIFIER USING CLASSICAL MACHINE LEARNING")

if st.button('Predict'):


    input_sms=st.text_input("Enter the message")

    transformed_sms=transform(input_sms)

    vector_input=tfidf.transform([transformed_sms])

    result=model.predict(vector_input)[0]

    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")


import streamlit as st
import joblib
test_model = joblib.load('sentiment_analyser')
st.title('Sentiment Analysis of customer reviews')
ip = st.text_input('Enter your review: ')
op = test_model.predict([ip])
if st.button('Sentiment Prediction'):
  st.title(op[0])
 

import streamlit as st
import helper
import pickle
import sklearn
from sklearn.feature_extraction.text import CountVectorizer

model = pickle.load(open('model.pkl', 'rb'))
st.header("Duplicate Question Pairs")

q1 = st.text_input("Enter question 1")
q2 = st.text_input("Enter question 2")

if st.button("Find"):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        st.header("Duplicate")
    else:
        st.header("Not Duplicate")
import plotly
import streamlit as st
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

sentiment = SentimentIntensityAnalyzer()

files = glob.glob('diaries/*')
st.header("Positivity")
negativity = []
positivity = []
for file in files:
    with open(file) as page:
        diary = page.read()
    scores = sentiment.polarity_scores(diary)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])
dates = [file.strip('diaries\\').strip('.txt') for file in files]
figure = px.line(x=dates, y=positivity, labels={'x': "Dates", 'y': "Positivity"})
st.plotly_chart(figure)

st.header("Negativity")
figure2 = px.line(x=dates, y=negativity, labels={'x': 'Dates', 'y': "Negativity"})
st.plotly_chart(figure2)

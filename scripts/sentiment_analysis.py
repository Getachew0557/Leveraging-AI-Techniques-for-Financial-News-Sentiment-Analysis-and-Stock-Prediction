import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from wordcloud import WordCloud
from textblob import TextBlob
import re

def preprocess_text(text):
    """
    Preprocess text by converting to lowercase, removing extra spaces, and removing punctuation.
    """
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def get_sentiment_score(text):
    return TextBlob(text).sentiment.polarity

def categorize_sentiment(score):
    if score > 0.1:
        return 'Positive'
    elif score < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

def analyze_sentiment(news_data):
    news_data['sentiment_score'] = news_data['headline'].apply(get_sentiment_score)
    news_data['sentiment'] = news_data['sentiment_score'].apply(categorize_sentiment)
    return news_data


    
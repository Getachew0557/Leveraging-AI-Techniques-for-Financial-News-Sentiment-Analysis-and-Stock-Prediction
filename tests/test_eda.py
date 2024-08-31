import os
import sys
import pytest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
import EDA as eda

@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing."""
    data = {
        'date': pd.date_range(start='2022-01-01', periods=100, freq='D'),
        'headline_length': range(100),
        'publisher': ['Publisher A'] * 50 + ['Publisher B'] * 50,
        'sentiment': [0.1 * i for i in range(100)],
        'sentiment_class': ['Positive' if i % 2 == 0 else 'Negative' for i in range(100)]
    }
    df = pd.DataFrame(data)
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    return df

def test_headlineLength(sample_df):
    """Test the headlineLength function."""
    try:
        eda.headlineLength(sample_df)
    except Exception as e:
        pytest.fail(f"headlineLength function failed with error: {e}")

def test_topPublisher(sample_df):
    """Test the topPublisher function."""
    try:
        eda.topPublisher(sample_df)
    except Exception as e:
        pytest.fail(f"topPublisher function failed with error: {e}")

# def test_convert_date(sample_df):
#     """Test the convert_date function."""
#     df = eda.convert_date(sample_df)
#     assert pd.api.types.is_datetime64_any_dtype(df['date']), "Date column should be in datetime format"
#     assert df['date'].notnull().all(), "Date column should not contain null values"

def test_yearlyArticlePublished(sample_df):
    """Test the yearlyArticlePublished function."""
    try:
        eda.yearlyArticlePublished(sample_df)
    except Exception as e:
        pytest.fail(f"yearlyArticlePublished function failed with error: {e}")

def test_daily_articles_published_each_month(sample_df):
    """Test the daily_articles_published_each_month function."""
    try:
        eda.daily_articles_published_each_month(sample_df)
    except Exception as e:
        pytest.fail(f"daily_articles_published_each_month function failed with error: {e}")

def test_threeYrJanu(sample_df):
    """Test the threeYrJanu function."""
    try:
        eda.threeYrJanu(sample_df)
    except Exception as e:
        pytest.fail(f"threeYrJanu function failed with error: {e}")

def test_articlePubYearly(sample_df):
    """Test the articlePubYearly function."""
    try:
        eda.articlePubYearly(sample_df)
    except Exception as e:
        pytest.fail(f"articlePubYearly function failed with error: {e}")

def test_numArticlePubTime(sample_df):
    """Test the numArticlePubTime function."""
    try:
        eda.numArticlePubTime(sample_df)
    except Exception as e:
        pytest.fail(f"numArticlePubTime function failed with error: {e}")

def test_sentimentScore(sample_df):
    """Test the sentimentScore function."""
    try:
        eda.sentimentScore(sample_df)
    except Exception as e:
        pytest.fail(f"sentimentScore function failed with error: {e}")

def test_sentimentClass(sample_df):
    """Test the sentimentClass function."""
    try:
        eda.sentimentClass(sample_df)
    except Exception as e:
        pytest.fail(f"sentimentClass function failed with error: {e}")

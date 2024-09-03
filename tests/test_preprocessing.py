# tests/test_preprocessing.py

import sys
import os
# Add the 'scripts' directory to the system path
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

import Preprocessing as dp

import pandas as pd
import talib


# Mock data for testing
data = {
    'Date': ['2024-08-01', '2024-08-02', '2024-08-03'],
    'Open': [100.0, 102.0, 101.0],
    'High': [105.0, 103.0, 104.0],
    'Low': [99.0, 101.0, 100.0],
    'Close': [104.0, 102.0, 103.0],
    'Volume': [1000, 1500, 2000],
    'headline': ['Stock rises', 'Market falls', 'Stable day']
}
df = pd.DataFrame(data)

def test_load_data():
    file_path = "data/AAPL_historical_data.csv"  # Update with a real or mock path
    loaded_df = dp.load_data(file_path)
    assert isinstance(loaded_df, pd.DataFrame)
    assert not loaded_df.empty

def test_summary_statistics():
    summary = dp.summary_statistics(df)
    assert isinstance(summary, pd.DataFrame)
    assert 'Open' in summary.columns

def test_check_missing_values():
    missing_values = dp.check_missing_values(df)
    assert isinstance(missing_values, pd.Series)
    assert missing_values.sum() == 0

def test_remove_columns():
    df_with_extra = df.copy()
    df_with_extra['Unnamed: 0'] = [0, 1, 2]
    cleaned_df = dp.remove_columns(df_with_extra)
    assert 'Unnamed: 0' not in cleaned_df.columns

def test_add_headline_length():
    df_with_length = dp.add_headline_length(df.copy())
    assert 'headline_length' in df_with_length.columns
    assert df_with_length['headline_length'].iloc[0] == len(df['headline'].iloc[0])

def test_get_headline_length_stats():
    df_with_length = dp.add_headline_length(df.copy())
    stats = dp.get_headline_length_stats(df_with_length)
    assert isinstance(stats, pd.Series)

def test_convert_date():
    df_converted = dp.convert_date(df.copy(), column_name='Date')
    assert isinstance(df_converted.index, pd.DatetimeIndex)
    assert 'Date' not in df_converted.columns
    assert len(df_converted.index) == len(df)  # Ensure the number of rows is unchanged
    assert df_converted.index.name == 'Date'  # Check that 'Date' is set as the index

def test_calculate_technical_indicators():
    df_with_indicators = dp.calculate_technical_indicators(df.copy())
    assert 'SMA_20' in df_with_indicators.columns
    assert 'RSI' in df_with_indicators.columns
    assert 'MACD' in df_with_indicators.columns

# Example to fetch stock data - Note: This requires internet connection and live data
def test_fetch_stock_data():
    historical_data = dp.fetch_stock_data('GOOG')
    assert isinstance(historical_data, pd.DataFrame)
    assert not historical_data.empty

# To calculate financial metrics. This requires internet connection and live data
def test_financial_metrics():
    metrics = dp.financial_metrics('GOOG')
    assert 'PE_Ratio' in metrics
    assert 'Market_Cap' in metrics
    assert 'Dividend_Yield' in metrics

# Note: The above two tests (`test_fetch_stock_data` and `test_financial_metrics`) involve live data
# fetching and may not be suitable for unit testing due to their reliance on external services.

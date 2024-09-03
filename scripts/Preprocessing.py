#import library
import os
import talib
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import pynance

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def summary_statistics(df):

    return df.describe()


def check_missing_values(df):

    return df.isnull().sum()


def remove_columns(df):

    return df.drop(columns=['Unnamed: 0'])


def add_headline_length(df):

    df['headline_length'] = df['headline'].apply(len)
    return df


def get_headline_length_stats(df):
    
    return df['headline_length'].describe()


def convert_date(df, column_name='Date'):
    """Convert a specified column to datetime."""
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")
    
    # Handle different formats for 'date' and 'Date'
    if column_name == 'date':
        df[column_name] = df[column_name].str.slice(0, 19)  # Adjust for specific formats if needed
    df[column_name] = pd.to_datetime(df[column_name]).dt.date
    
    # If you want to set this column as the index, uncomment the line below:
    # df.set_index(column_name, inplace=True)
    
    return df

def calculate_technical_indicators(df):
    """Calculate basic technical indicators using TA-Lib."""
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return df

def plot_stock_data(df):
    """Plot the stock data with technical indicators."""
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['Close'], label='Close', color='blue')
    plt.plot(df.index, df['SMA_20'], label='20-day SMA', color='red')
    plt.plot(df.index, df['SMA_50'], label='50-day SMA', color='green')
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_rsi(df):
    """Plot the Relative Strength Index (RSI)."""
    plt.figure(figsize=(14, 5))
    plt.plot(df.index, df['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought')
    plt.axhline(30, color='green', linestyle='--', label='Oversold')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_macd(df):
    """Plot the Moving Average Convergence Divergence (MACD)."""
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['MACD'], label='MACD', color='blue')
    plt.plot(df.index, df['MACD_signal'], label='MACD Signal', color='red')
    plt.bar(df.index, df['MACD_hist'], label='MACD Histogram', color='gray', alpha=0.3)
    plt.title('MACD and Signal Line')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

def fetch_stock_data(ticker, period='1y'):
    """Fetch historical stock data using yfinance."""
    stock_data = yf.Ticker(ticker)
    historical_data = stock_data.history(period=period)
    return historical_data

def financial_metrics(ticker):
    """Calculate financial metrics using yfinance."""
    metrics = {}
    stock = yf.Ticker(ticker)
    
    # Fetching company information
    info = stock.info
    metrics['PE_Ratio'] = info.get('forwardEps', 'N/A') / info.get('forwardEps', 'N/A') if info.get('forwardEps', None) else 'N/A'
    metrics['Market_Cap'] = info.get('marketCap', 'N/A')
    metrics['Dividend_Yield'] = info.get('dividendYield', 'N/A')
    
    return metrics



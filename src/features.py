"""
Feature engineering utilities for stock market data.
"""

import pandas as pd
import numpy as np


def calculate_rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Relative Strength Index."""
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def calculate_macd(
    prices: pd.Series,
    fast: int = 12,
    slow: int = 26,
    signal: int = 9
) -> tuple:
    """Calculate MACD indicator."""
    ema_fast = prices.ewm(span=fast, adjust=False).mean()
    ema_slow = prices.ewm(span=slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line


def calculate_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate technical indicators and features.
    
    Args:
        df: DataFrame with OHLCV data
        
    Returns:
        DataFrame with additional feature columns
    """
    df = df.copy()
    
    # Price returns
    df['return_1d'] = df['Close'].pct_change()
    df['return_5d'] = df['Close'].pct_change(5)
    df['return_20d'] = df['Close'].pct_change(20)
    
    # Moving averages
    df['ma_5'] = df['Close'].rolling(5).mean()
    df['ma_20'] = df['Close'].rolling(20).mean()
    df['ma_50'] = df['Close'].rolling(50).mean()
    
    # Price relative to MA
    df['price_to_ma5'] = df['Close'] / df['ma_5']
    df['price_to_ma20'] = df['Close'] / df['ma_20']
    
    # Technical indicators
    df['rsi'] = calculate_rsi(df['Close'])
    df['macd'], df['macd_signal'] = calculate_macd(df['Close'])
    df['macd_diff'] = df['macd'] - df['macd_signal']
    
    # Volatility
    df['volatility'] = df['return_1d'].rolling(20).std()
    
    # Volume features
    df['volume_ma20'] = df['Volume'].rolling(20).mean()
    df['volume_ratio'] = df['Volume'] / df['volume_ma20']
    
    # Target variable
    df['next_return'] = df['return_1d'].shift(-1)
    
    return df


def create_target(df: pd.DataFrame, threshold: float = 0.005) -> pd.DataFrame:
    """
    Create classification target (UP/DOWN/STABLE).
    
    Args:
        df: DataFrame with 'next_return' column
        threshold: Movement threshold (default 0.5%)
        
    Returns:
        DataFrame with 'target' column
    """
    df = df.copy()
    df['target'] = 'STABLE'
    df.loc[df['next_return'] > threshold, 'target'] = 'UP'
    df.loc[df['next_return'] < -threshold, 'target'] = 'DOWN'
    return df

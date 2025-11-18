"""
Data loading utilities for stock market data.
"""

import yfinance as yf
import pandas as pd
from datetime import datetime
from typing import List, Dict


def download_stock_data(
    tickers: List[str],
    start: str = '2018-01-01',
    end: str = None
) -> Dict[str, pd.DataFrame]:
    """
    Download historical stock data from Yahoo Finance.
    
    Args:
        tickers: List of stock ticker symbols
        start: Start date (YYYY-MM-DD)
        end: End date (YYYY-MM-DD), defaults to today
        
    Returns:
        Dictionary mapping ticker to DataFrame
    """
    if end is None:
        end = datetime.now().strftime('%Y-%m-%d')
    
    data_dict = {}
    
    for ticker in tickers:
        try:
            df = yf.download(ticker, start=start, end=end, progress=False)
            data_dict[ticker] = df
            print(f"✓ {ticker}: {len(df)} records")
        except Exception as e:
            print(f"✗ Error downloading {ticker}: {e}")
    
    return data_dict


def combine_stock_data(data_dict: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Combine multiple stock DataFrames into a single DataFrame.
    
    Args:
        data_dict: Dictionary mapping ticker to DataFrame
        
    Returns:
        Combined DataFrame with 'Stock' column
    """
    dfs = []
    
    for ticker, df in data_dict.items():
        df_copy = df.copy()
        df_copy['Stock'] = ticker
        df_copy = df_copy.reset_index()
        dfs.append(df_copy)
    
    combined = pd.concat(dfs, ignore_index=True)
    return combined

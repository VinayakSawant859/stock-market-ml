# 📈 Stock Market Prediction & Anomaly Detection System

A machine learning project for predicting stock price movements and detecting unusual trading patterns in the Indian stock market.

## 🎯 Project Overview

This project implements an AI-powered system that:
- **Predicts** next-day stock price movements (UP/DOWN/STABLE) using machine learning
- **Detects** anomalous trading patterns that could indicate unusual market activity
- **Explains** predictions using SHAP and LIME for model interpretability
- **Visualizes** technical indicators and market trends

## 🚀 Features

- **Multi-Stock Analysis**: Analyzes TCS, Infosys, HDFC Bank, and Reliance against Nifty50
- **Technical Indicators**: RSI, MACD, Moving Averages, Volume ratios, Volatility measures
- **ML Models**: Random Forest for classification, Isolation Forest for anomaly detection
- **Explainable AI**: SHAP values and LIME explanations for model transparency
- **Interactive Visualizations**: Price charts, technical indicators, confusion matrices

## 📊 Tech Stack

- **Python 3.10+**
- **Data Collection**: yfinance
- **Data Processing**: pandas, numpy
- **Machine Learning**: scikit-learn
- **Explainability**: SHAP, LIME
- **Visualization**: matplotlib, seaborn, plotly

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/VinayakSawant859/stock-market-ml.git
cd stock-market-ml
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Running the Notebook

Open the Jupyter notebook:
```bash
jupyter notebook market_insights_fresher.ipynb
```

Or use Google Colab:
1. Upload `market_insights_fresher.ipynb` to Google Drive
2. Open with Google Colab
3. Run all cells

### Quick Start

```python
# Download stock data
from src.data_loader import download_stock_data

stocks = ['TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'RELIANCE.NS']
data = download_stock_data(stocks, start='2018-01-01')

# Calculate features
from src.features import calculate_features

features_df = calculate_features(data)

# Train model
from src.models import train_prediction_model

model = train_prediction_model(features_df)

# Make predictions
predictions = model.predict(latest_data)
```

## 📁 Project Structure

```
stock-market-ml/
├── market_insights_fresher.ipynb    # Main analysis notebook
├── README.md                         # Project documentation
├── requirements.txt                  # Python dependencies
├── LICENSE                          # MIT License
├── .gitignore                       # Git ignore rules
├── data/                            # Data directory (gitignored)
│   ├── raw/                         # Raw downloaded data
│   └── processed/                   # Processed features
├── models/                          # Saved models (gitignored)
│   ├── rf_model.pkl
│   ├── scaler.pkl
│   └── anomaly_detector.pkl
├── src/                            # Source code
│   ├── __init__.py
│   ├── data_loader.py              # Data download utilities
│   ├── features.py                 # Feature engineering
│   ├── models.py                   # ML models
│   └── visualization.py            # Plotting functions
├── notebooks/                      # Additional notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_experiments.ipynb
├── tests/                          # Unit tests
│   ├── test_data_loader.py
│   ├── test_features.py
│   └── test_models.py
└── docs/                           # Additional documentation
    ├── methodology.md
    └── deployment.md
```

## 🔍 Methodology

### 1. Data Collection
- Fetch historical stock data from Yahoo Finance (2018-present)
- Daily OHLCV data for major Indian stocks
- Compare against Nifty50 benchmark

### 2. Feature Engineering
- **Price Features**: Returns (1d, 5d, 20d), Moving averages (MA-5, MA-20, MA-50)
- **Technical Indicators**: RSI, MACD, MACD Signal
- **Volatility**: Rolling standard deviation
- **Volume**: Volume ratios, volume moving average

### 3. Model Training
- **Classification**: Random Forest with 100 estimators
- **Target**: Next-day movement (UP/DOWN/STABLE with ±0.5% threshold)
- **Split**: Time-based 80/20 train-test split
- **Evaluation**: Accuracy, Precision, Recall, F1-score

### 4. Anomaly Detection
- Isolation Forest with 5% contamination threshold
- Detects unusual trading patterns based on all features
- Highlights potential market manipulation or extreme events

## 📈 Results

- **Prediction Accuracy**: ~55-60% on test set
- **Best Features**: RSI, MACD, short-term returns, volume ratios
- **Anomaly Detection**: Successfully identifies unusual trading days
- **Model Explainability**: SHAP values show feature importance

### Sample Confusion Matrix
```
              Predicted
           UP   DOWN  STABLE
Actual UP    120   30     50
      DOWN    35  110     55
    STABLE    45   40    115
```

## 🎓 Key Learnings

1. **Financial data is inherently noisy** - Even good models have limited accuracy
2. **Feature engineering matters** - Technical indicators significantly improve performance
3. **Time-series requires special handling** - No random splits, sequential validation needed
4. **Explainability is crucial** - Traders need to understand why predictions are made

## 🔮 Future Improvements

- [ ] Add LSTM/Transformer models for sequential patterns
- [ ] Incorporate news sentiment analysis
- [ ] Include options data (implied volatility)
- [ ] Real-time prediction API with FastAPI
- [ ] Automated retraining pipeline
- [ ] Backtesting framework for strategy evaluation
- [ ] Multi-timeframe analysis (intraday + daily)
- [ ] Portfolio optimization features

## 🚀 Deployment Ideas

### Architecture Overview
```
Yahoo Finance API → Data Pipeline → Feature Engineering → ML Models → API
                                                                      ↓
                                                            Web Dashboard
                                                            Alert System
```

### Tech Stack for Production
- **API**: FastAPI
- **Database**: PostgreSQL
- **Scheduling**: Apache Airflow
- **Monitoring**: Prometheus + Grafana
- **Deployment**: Docker + AWS/Azure
- **MLOps**: MLflow for model versioning

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Vinayak Sawant**
- GitHub: [@VinayakSawant859](https://github.com/VinayakSawant859)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/vinayaksawant859)
- Email: vinayaksawant859@gmail.com

## 🙏 Acknowledgments

- Yahoo Finance for providing free stock data
- scikit-learn community for excellent ML tools
- SHAP and LIME libraries for explainability
- Indian stock market for being an interesting dataset

## ⚠️ Disclaimer

This project is for educational and research purposes only. It is NOT financial advice. Do not use these predictions for actual trading without proper risk management and professional consultation.

---

⭐ If you found this project helpful, please consider giving it a star!

**Last Updated**: November 2025

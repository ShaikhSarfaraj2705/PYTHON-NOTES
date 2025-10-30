from flask import Flask, render_template, request

import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import requests

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    # Example: Top stocks
    top_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    data = []
    for stock in top_stocks:
        ticker = yf.Ticker(stock)
        info = ticker.info
        data.append({
            'symbol': stock,
            'price': info['currentPrice'],
            'change': info.get('regularMarketChangePercent', 0)
        })
    return render_template('index.html', stocks=data)

# Stock Details Page
@app.route('/stock/<symbol>')
def stock_details(symbol):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="1y") 
    # Plot candlestick chart
    fig = go.Figure(data=[go.Candlestick(
        x=hist.index,
        open=hist['Open'],
        high=hist['High'],
        low=hist['Low'],
        close=hist['Close']
    )])
    chart = fig.to_html(full_html=False)
    info = ticker.info
    return render_template('stock_details.html', symbol=symbol, chart=chart, info=info)

# Market Analysis Page
@app.route('/market-analysis')
def market_analysis():
    import numpy as np  # (or put this at the top of file)
    sectors = ['Technology', 'Finance', 'Healthcare']
    performance = {s: round(100 * (0.9 + 0.2 * np.random.rand()), 2) for s in sectors}
    return render_template('market_analysis.html', performance=performance)

# Portfolio Page
@app.route('/portfolio')
def portfolio():
    # Mock portfolio data
    portfolio_data = [
        {'symbol': 'AAPL', 'shares': 10, 'price': 180},
        {'symbol': 'TSLA', 'shares': 5, 'price': 900},
    ]
    return render_template('portfolio.html', portfolio=portfolio_data)

# News Page
@app.route('/news')
def news():
    url = 'https://newsapi.org/v2/top-headlines?category=business&apiKey=YOUR_API_KEY'
    response = requests.get(url).json()
    articles = response.get('articles', [])
    return render_template('news.html', articles=articles)

# Prediction Page
@app.route('/prediction')
def prediction():
    # Example placeholder
    predicted_prices = {'AAPL': 200, 'TSLA': 950}
    return render_template('prediction.html', predicted=predicted_prices)

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

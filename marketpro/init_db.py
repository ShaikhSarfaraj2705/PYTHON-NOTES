from models import db, MarketIndex, Stock, PricePoint, Holding, NewsArticle
from app import app
from datetime import datetime, timedelta


with app.app_context():
db.drop_all()
db.create_all()


# sample indices
sp = MarketIndex(name='S&P 500', symbol='^GSPC', last_price=661.82, change_pct=0.56)
nas = MarketIndex(name='NASDAQ Composite', symbol='^IXIC', last_price=595.97, change_pct=0.42)
dj = MarketIndex(name='Dow Jones', symbol='^DJI', last_price=462.28, change_pct=0.63)
db.session.add_all([sp,nas,dj])


# sample stock + price timeseries (synthetic) for SPY
s = Stock(symbol='SPY', name='S&P 500 ETF')
db.session.add(s)
db.session.flush()
base = datetime.utcnow() - timedelta(days=30)
import random
price = 4800
for i in range(30):
price += random.uniform(-30,30)
pp = PricePoint(stock_id=s.id, ts=base + timedelta(days=i), open=price-5, high=price+8, low=price-10, close=price, volume=1000000)
db.session.add(pp)


# empty holdings
h = Holding(symbol='AAPL', shares=10, avg_cost=150.0)
db.session.add(h)


# sample news
na = NewsArticle(title='Wall Street rebounds', summary='U.S. stocks rebounded...', source='AP News', published_at=datetime.ut
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class MarketIndex(db.Model):
__tablename__ = 'market_index'
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(64), nullable=False, unique=True)
symbol = db.Column(db.String(16), nullable=True)
last_price = db.Column(db.Float)
change_pct = db.Column(db.Float)
updated_at = db.Column(db.DateTime, default=datetime.utcnow)


class Stock(db.Model):
__tablename__ = 'stock'
id = db.Column(db.Integer, primary_key=True)
symbol = db.Column(db.String(16), nullable=False, unique=True)
name = db.Column(db.String(128))


class PricePoint(db.Model):
__tablename__ = 'price_point'
id = db.Column(db.Integer, primary_key=True)
stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
ts = db.Column(db.DateTime, index=True)
open = db.Column(db.Float)
high = db.Column(db.Float)
low = db.Column(db.Float)
close = db.Column(db.Float)
volume = db.Column(db.BigInteger)


class Holding(db.Model):
__tablename__ = 'holding'
id = db.Column(db.Integer, primary_key=True)
symbol = db.Column(db.String(16), nullable=False)
shares = db.Column(db.Float, nullable=False)
avg_cost = db.Column(db.Float, nullable=False)


class NewsArticle(db.Model):
__tablename__ = 'news'
id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(256))
summary = db.Column(db.Text)
source = db.Column(db.String(128))
published_at = db.Column(db.DateTime)
url = db.Column(db.String(512))
from flask import Blueprint, jsonify, request
from models import db, MarketIndex, PricePoint, Stock, Holding, NewsArticle
from sqlalchemy import desc, func


api_bp = Blueprint('api', __name__)


@api_bp.route('/indices')
def indices():
rows = MarketIndex.query.all()
data = [{
'name': r.name, 'symbol': r.symbol, 'last_price': r.last_price, 'change_pct': r.change_pct
} for r in rows]
return jsonify(data)


@api_bp.route('/stock/<symbol>/history')
def stock_history(symbol):
s = Stock.query.filter(func.lower(Stock.symbol) == symbol.lower()).first()
if not s:
return jsonify({'error': 'Unknown symbol'}), 404
pts = PricePoint.query.filter_by(stock_id=s.id).order_by(PricePoint.ts).all()
out = [{'ts': p.ts.isoformat(), 'open': p.open, 'high': p.high, 'low': p.low, 'close': p.close, 'volume': p.volume} for p in pts]
return jsonify(out)


@api_bp.route('/portfolio')
def portfolio():
holdings = Holding.query.all()
# compute totals simply here
data = []
for h in holdings:
data.append({'symbol': h.symbol, 'shares': h.shares, 'avg_cost': h.avg_cost})
return jsonify({'holdings': data})


@api_bp.route('/news')
def news_list():
articles = NewsArticle.query.order_by(desc(NewsArticle.published_at)).limit(20).all()
out = [{'title': a.title, 'summary': a.summary, 'source': a.source, 'published_at': a.published_at.isoformat(), 'url': a.url} for a in articles]
return jsonify(out)
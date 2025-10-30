window.app = {
async init(){
await this.loadIndices();
await this.loadSP500();
await this.loadNews();
},


async loadIndices(){
const res = await fetch('/api/indices');
const list = await res.json();
const container = document.getElementById('indices-row');
container.innerHTML = '';
list.forEach(ix => {
const el = document.createElement('div'); el.className='card index-card';
el.innerHTML = `<strong>${ix.name}</strong><div class="price">${ix.last_price}</div><div class="pct">${ix.change_pct}%</div>`;
container.appendChild(el);
});
},


async loadSP500(){
// for demo we'll use a symbol like SPY or synthetic sample
const symbol = 'SPY';
const res = await fetch(`/api/stock/${symbol}/history`);
if(!res.ok) return;
const pts = await res.json();
const x = pts.map(p=>p.ts);
const y = pts.map(p=>p.close);
const trace = { x, y, type:'scatter', mode:'lines', name:'SP500' };
const layout = { margin:{t:20}, paper_bgcolor:'rgba(0,0,0,0)', plot_bgcolor:'rgba(0,0,0,0)' };
Plotly.newPlot('sp500-chart',[trace], layout, {responsive:true});
},


async loadNews(){
const res = await fetch('/api/news');
const news = await res.json();
const c = document.getElementById('news-list');
c.innerHTML = news.map(a=>`<div class="article"><h4>${a.title}</h4><p>${a.summary}</p></div>`).join('\n');
}
}
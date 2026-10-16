import json,html
d=json.load(open('data.json'))
f=lambda x:"R$ "+f"{x:,.2f}".replace(",","X").replace(".",",").replace("X",".")
p=d['price']
def dist(m): return (p/m-1)*100
rows=""
alerts=[]
for n,m in (("MA50",d['ma50']),("MA200",d['ma200'])):
    x=dist(m); cls="warn" if abs(x)<=2 else ""
    if abs(x)<=2: alerts.append(f"Preço a {abs(x):.2f}% da {n}".replace(".",","))
    rows+=f'<div class="row {cls}"><span>{n} (diária)</span><b>{f(m)}</b><i>{x:+.2f}%</i></div>'.replace(".",",",0)
rows=rows
E=html.escape
al="".join(f'<div class="alert">⚠ {a}</div>' for a in alerts)
news="".join(f'<li><a href="{u}" target="_blank" rel="noopener">{E(t)}</a><small>{E(s)} · {dt}</small></li>' for t,s,dt,u in d['news'])
tg="".join(f'<div class="row"><span>{a}</span><b>{b}</b><i>{c}</i></div>' for a,b,c in d['targets'])
src=" · ".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n,u in d['sources'])
sign=lambda x:f"{x:+.2f}%".replace(".",",")
out=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>O.S Mercado · VBBR3</title>
<style>*{{box-sizing:border-box}}body{{margin:0;background:#0b0f14;color:#e6edf3;font:16px/1.45 system-ui,sans-serif;padding:14px;max-width:640px;margin:auto}}
h1{{font-size:18px;margin:4px 0}}.card{{background:#141a22;border:1px solid #222c38;border-radius:14px;padding:14px;margin:12px 0}}
.big{{font-size:34px;font-weight:700}}.up{{color:#3fb950}}.row{{display:flex;justify-content:space-between;gap:8px;padding:6px 0;border-bottom:1px solid #1f2833}}.row i{{font-style:normal;color:#8b98a5}}
.warn{{color:#f0b429}}.alert{{background:#3a2d0a;color:#f0b429;border-radius:10px;padding:8px 10px;margin-bottom:8px;font-weight:600}}
small,.mut{{color:#8b98a5;font-size:13px}}a{{color:#58a6ff}}li{{margin:0 0 10px;list-style:none}}ul{{padding:0;margin:0}}li small{{display:block}}
.rec{{font-size:22px;font-weight:700;color:#3fb950}}h2{{font-size:14px;text-transform:uppercase;letter-spacing:.06em;color:#8b98a5;margin:0 0 8px}}</style></head><body>
<h1>O.S Mercado · VBBR3 — Vibra Energia</h1><div class="mut">Atualizado em {d['updated']} (Brasília)</div>
<div class="card">{al}<div class="big">{f(p)} <span class="up" style="font-size:18px">{sign(d['change_pct'])}</span></div>
<div class="mut">{d['price_label']}</div><p class="mut">⚠ {E(d['alt_price'])}</p>
<div class="row"><span>Fechamento anterior</span><b>{f(d['prev_close'])}</b><i>{d['prev_src']}</i></div>
<div class="row"><span>Máxima 52 sem.</span><b>{f(d['high52'])}</b><i></i></div></div>
<div class="card"><h2>Médias móveis</h2>{rows}<p class="mut">Fonte: {d['ma_src']}. {E(d['ma_alt'])} Alerta quando distância ≤ 2%.</p></div>
<div class="card"><h2>Suporte / Resistência</h2><div class="row"><span>Suporte</span><b>{f(d['support'])}</b><i>{sign(dist(d['support']) *-1 if False else (d['support']/p-1)*100)}</i></div><div class="row"><span>Resistência</span><b>{f(d['resistance'])}</b><i>{sign((d['resistance']/p-1)*100)}</i></div><p class="mut">Fonte: {d['sr_src']}</p></div>
<div class="card"><h2>Volume</h2><p>{E(d['volume'])}</p></div>
<div class="card"><h2>Analistas</h2><p>{E(d['consensus'])}</p>{tg}</div>
<div class="card"><h2>Notícias</h2><ul>{news}</ul></div>
<div class="card"><h2>Indicação</h2><div class="rec">{d['rec']}</div><p>{E(d['reason'])}</p></div>
<div class="card"><h2>Fontes</h2><p class="mut">{src}</p><p class="mut">Dados de agregadores públicos, com possível atraso; não é cotação em tempo real. Onde há conflito, está indicado.</p></div>
<p><b>Isso não é aconselhamento financeiro. A decisão e o risco são exclusivamente do investidor.</b></p></body></html>'''
open('site/index.html','w').write(out)

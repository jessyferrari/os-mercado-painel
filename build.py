import json,html
from datetime import datetime,timezone,timedelta
d=json.load(open('data.json'))
E=html.escape
f=lambda x:"R$ "+f"{x:,.2f}".replace(",","X").replace(".",",").replace("X",".")
sign=lambda x:f"{x:+.2f}%".replace(".",",")
p=d['price']
dist=lambda m:(p/m-1)*100
rows="";alerts=[]
for n,m in (("MA50",d['ma50']),("MA200",d['ma200'])):
    x=dist(m);w=abs(x)<=2
    if w: alerts.append(f"Preço a {abs(x):.2f}% da {n}".replace(".",","))
    rows+=f'<div class="row {"warn" if w else ""}"><span>{n} (diária)</span><b class="num">{f(m)}</b><i>{sign(x)}</i></div>'
al="".join(f'<div class="alert">⚠ {a}</div>' for a in alerts)
BR=timezone(timedelta(hours=-3))
def parse(s):
    if len(s)>10: return datetime.fromisoformat(s).astimezone(BR),True
    return datetime.fromisoformat(s+"T00:00:00-03:00"),False
items=[]
for n in d['news']:
    dt,h=parse(n['publicado_em']); items.append((dt,h,n))
items.sort(key=lambda t:t[0],reverse=True)
def card(dt,h,n):
    when=dt.strftime("%d/%m/%Y")+(dt.strftime(" %H:%M")+" (Brasília)" if h else " • hora não informada")
    return (f'<a class="ncard" href="{E(n["url"])}" target="_blank" rel="noopener"><span class="arrow">➤</span><span class="nb">'
            f'<span class="ntime">{when}</span><span class="ntitle">{E(n["titulo"])}</span><span class="nsrc">{E(n["fonte"])}</span></span></a>')
def when(dt,h): return dt.strftime("%H:%M") if h else dt.strftime("%d/%m")
def card(dt,h,n):
    w=dt.strftime("%d/%m/%Y")+(dt.strftime(" %H:%M")+" (Brasília)" if h else " • hora não informada")
    return (f'<a class="nitem" href="{E(n["url"])}" target="_blank" rel="noopener"><span class="ntime">{w}</span><span class="ntitle">{E(n["titulo"])}</span><span class="nsrc">{E(n["fonte"])} ➤ abrir matéria</span></a>')
cards="".join(card(*t) for t in items)
ticker="".join(f'<div class="tit"><span class="tt">{when(dt,h)}</span><span class="ts">{E(n["fonte"])}</span><span class="tx">{E(n["titulo"])}</span></div>' for dt,h,n in items[:10])
tg="".join(f'<div class="row"><span>{a}</span><b>{b}</b><i>{c}</i></div>' for a,b,c in d['targets'])
src=" · ".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n,u in d['sources'])
sr=lambda v:sign((v/p-1)*100)
T=open('template.html').read()
rep={'@@UPDATED@@':d['updated'],'@@ALERTS@@':al,'@@PRICE@@':f(p),'@@CHG@@':sign(d['change_pct']),'@@PLABEL@@':E(d['price_label']),
'@@ALT@@':E(d['alt_price']),'@@PREV@@':f(d['prev_close']),'@@PREVSRC@@':E(d['prev_src']),'@@H52@@':f(d['high52']),'@@ROWS@@':rows,
'@@MASRC@@':E(d['ma_src']),'@@MAALT@@':E(d['ma_alt']),'@@SUP@@':f(d['support']),'@@SUPD@@':sr(d['support']),'@@RES@@':f(d['resistance']),
'@@RESD@@':sr(d['resistance']),'@@SRSRC@@':E(d['sr_src']),'@@VOL@@':E(d['volume']),'@@CONS@@':E(d['consensus']),'@@TG@@':tg,
'@@CARDS@@':cards,'@@TICKER@@':ticker,'@@REC@@':d['rec'],'@@REASON@@':E(d['reason']),'@@SRC@@':src}
for k,v in rep.items(): T=T.replace(k,v)
T=T.replace(' \u2014 ',' • ').replace(' \u2013 ',' • ').replace('\u2014','•').replace('\u2013','•')
open('index.html','w').write(T)

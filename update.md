# Redeploy do painel O.S Mercado (VBBR3)
Público: https://jessyferrari.github.io/os-mercado-painel/  (GitHub Pages, repo jessyferrari/os-mercado-painel, branch main, raiz)
1. Buscar dados reais (WebSearch/WebFetch): cotação (Renova Invest/ADVFN/BolsaData), MA50/200 (QuantBrasil, Toolz), suporte/resistência (Toolz), consenso (ADVFN), notícias. Nunca inventar; registrar conflitos.
2. Editar /workspace/os-mercado-painel/data.json (campos: updated, price, change_pct, ma50, ma200, news, etc.). "updated" em horário de Brasília.
3. python3 build.py  -> gera index.html (alerta automático se distância <=2% de MA50/MA200).
4. git add -A && git commit -m "update HH:MM" && git push   (gh já autenticado como jessyferrari)
5. Pages republica em ~1 min. Verificar com WebFetch.
Netlify (site os-mercado-vbbr3, id b86bbbc3-15d5-4c1e-a6e1-f987cb74a1aa) está sem créditos: deploy falha com "Skipped due to account credit usage exceeded".

## Regras permanentes
1. Nunca usar travessão (—) nem meia-risca (–). Usar • no lugar (build.py sanitiza a saída).
2. O painel começa com a linha "Cliente: Antonio de A. C.".

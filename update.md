# Redeploy do painel O.S Mercado (VBBR3)
Público: https://jessyferrari.github.io/os-mercado-painel/  (GitHub Pages, repo jessyferrari/os-mercado-painel, branch main, raiz)
1. Buscar dados reais (WebSearch/WebFetch): cotação (Renova Invest/ADVFN/BolsaData), MA50/200 (QuantBrasil, Toolz), suporte/resistência (Toolz), consenso (ADVFN), notícias. Nunca inventar; registrar conflitos.
2. Editar /workspace/os-mercado-painel/data.json (campos: updated, price, change_pct, ma50, ma200, news, etc.). "updated" em horário de Brasília.
3. python3 build.py  -> lê data.json + template.html e gera index.html (alerta automático se distância <=2% de MA50/MA200).
4. git add -A && git commit -m "update HH:MM" && git push   (gh já autenticado como jessyferrari)
5. Pages republica em ~1 min. Verificar com WebFetch.
Netlify (site os-mercado-vbbr3, id b86bbbc3-15d5-4c1e-a6e1-f987cb74a1aa) está sem créditos: deploy falha com "Skipped due to account credit usage exceeded".

## Regras permanentes
1. Nunca usar travessão (—) nem meia-risca (–). Usar • no lugar (build.py sanitiza a saída).
2. O painel começa com a linha "Cliente: Antonio de A. C.".
3. Não aparecer nenhum — ou – no index.html (build.py sanitiza; conferir com grep após o deploy).
4. Ressalva obrigatória no rodapé: "Isso não é aconselhamento financeiro. A decisão e o risco são exclusivamente do investidor."

## Estrutura (redesenho tech/neon)
- template.html: layout, CSS neon e JS. Edite o visual aqui; build.py só preenche os @@MARCADORES@@.
- Relógio ao vivo no topo (acima do preço): JS com Intl, fuso America/Sao_Paulo, rótulo "Horário de Brasília", data completa e HH:MM:SS a cada segundo.
- data.json "news" é uma lista de objetos: {"titulo","fonte","url","publicado_em"}. publicado_em em ISO com fuso (ex. "2026-10-16T17:41:00-03:00"); se a fonte não informar a hora, usar só a data ("2026-10-16") e o painel mostra "hora não informada". Nunca inventar hora. Verificar data/hora com WebFetch na matéria.
- build.py ordena por publicado_em (mais recentes primeiro). Rotinas apenas ADICIONAM itens (e podem remover os mais antigos; manter pelo menos 8).
- Seção "Últimas notícias": cartões neon com seta ➤, data/hora, título, fonte e link; rolagem automática lenta (~30 px/s, constante SPEED no template), pausa ao tocar/hover/rolar e retoma após 3 s.

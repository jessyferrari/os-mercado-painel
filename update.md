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

## Estrutura (layout sóbrio, v3)
- template.html: layout, CSS e JS. build.py só preenche os @@MARCADORES@@ (@@TICKER@@ = linhas da faixa, @@CARDS@@ = lista do painel).
- Relógio: barra compacta (52px) com HH:MM:SS e data de Brasília ao vivo (Intl, America/Sao_Paulo), leve brilho só no relógio.
- Faixa "Últimas notícias" logo abaixo do relógio e acima do preço: altura de 1 linha (40px), fundo neon ciano/azul escuro, loop vertical contínuo, 4,5 s por notícia (transição de 0,6 s), mostra HH:MM (ou dd/mm se sem hora) + fonte + título (10 mais recentes). Seta ▾/▴ à direita. Clicar na seta ou na faixa expande painel com lista completa (título, fonte, data/hora de Brasília, link). Fecha clicando na seta de novo ou fora do painel. prefers-reduced-motion: sem animação (mostra a mais recente).
- Cores: títulos de seção e contornos dos cartões em dourado (#D4AF37). Sem magenta. Neon forte só na faixa de notícias.
- data.json "news": lista de {"titulo","fonte","url","publicado_em"}. publicado_em em ISO com fuso (ex. "2026-10-16T17:41:00-03:00"); sem hora na fonte, só a data ("2026-10-16"), painel mostra "hora não informada". Nunca inventar hora; verificar na matéria (datePublished/WebFetch). build.py ordena por data/hora (mais recentes primeiro). Rotinas só ADICIONAM itens (manter pelo menos 8).
- Validar JS: extrair <script> do index.html e rodar node --check.

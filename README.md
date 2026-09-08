# Trivia Master

Jogo de trivia sobre bandeiras, capitais, política e cultura, em português e inglês.

## Como funciona

O site é feito só com HTML, CSS e JavaScript puro, sem framework e sem etapa de build. As perguntas ficam em arquivos JSON dentro da pasta `data/`, carregados direto pelo navegador.

Categorias disponíveis:

- Bandeiras
- Capitais
- Política & Cultura
- Todos (mistura as três anteriores)

Cada partida sorteia 10 perguntas da categoria escolhida, com 4 alternativas cada. No fim da rodada aparece a pontuação e dá pra jogar de novo ou trocar de categoria. Não tem login nem histórico salvo, tudo fica só na memória da página.

## Rodando localmente

Como o navegador bloqueia o carregamento de arquivos JSON locais via `file://`, para testar localmente é preciso subir um servidor simples na pasta do projeto:

```
python3 -m http.server 8000
```

Depois é só abrir `http://localhost:8000` no navegador.

## Estrutura de arquivos

```
index.html
css/style.css
js/i18n.js
js/app.js
data/bandeiras.json
data/capitais.json
data/politica-cultura.json
scripts/          (scripts usados para gerar o banco de perguntas, não são necessários pro site funcionar)
```

## Publicando no GitHub Pages

1. Suba todos os arquivos deste projeto para a raiz do repositório.
2. No GitHub, vá em Settings > Pages.
3. Em "Source", escolha a branch principal (geralmente `main`) e a pasta `/ (root)`.
4. Salve. Em alguns minutos o site fica disponível em `https://<seu-usuario>.github.io/<nome-do-repositorio>/`.

## Expandindo o banco de perguntas

Os scripts em `scripts/` (Python) foram usados para gerar os arquivos JSON de perguntas a partir da lista de países em `scripts/countries.json` e de uma lista de fatos de política e cultura escrita diretamente no script `build_politica_cultura.py`. Pra adicionar mais perguntas de política e cultura, basta editar esse script (usando a função `add(...)`) e rodar `python3 build_politica_cultura.py` de dentro da pasta `scripts/`.

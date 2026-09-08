# Trivia Master

Jogo de trivia sobre bandeiras, capitais, política e cultura, em português e inglês.

## Como funciona

O site é feito só com HTML, CSS e JavaScript puro, sem framework e sem etapa de build. As perguntas ficam em arquivos JSON dentro da pasta `data/`, carregados direto pelo navegador.

Categorias disponíveis:

- Bandeiras
- Capitais
- Política & Cultura
- Todos (mistura as três anteriores)

O jogo tem dois modos, escolhidos na tela inicial. Eles não compartilham estado: o que acontece em um não afeta o outro.

### Modo clássico

Cada partida sorteia 10 perguntas da categoria escolhida, com 4 alternativas cada. No fim da rodada aparece a pontuação e dá pra jogar de novo ou trocar de categoria. Não tem vidas, loja nem progressão, tudo fica só na memória da página.

### Modo roguelite

Um modo de sobrevivência com perguntas de todas as categorias misturadas:

- A run começa com 3 vidas. Cada erro custa uma vida e a run acaba quando elas zeram.
- Cada acerto rende **energia**, a moeda da run. A partir do terceiro acerto seguido entra um bônus de sequência, que cresce até +3 por acerto.
- Entre uma pergunta e outra dá pra abrir a **loja de facilidades** e gastar energia em cartas (elimina duas alternativas erradas), dica, pular a pergunta, escudo (absorve o próximo erro) e recuperar uma vida. O preço de cada item sobe a cada compra dentro da mesma run.
- No fim da run, uma fatia da energia acumulada vira **cristais**, a moeda permanente.

### Progressão permanente

Os cristais ficam salvos no navegador e são gastos na tela de progressão, acessível pela tela inicial. São quatro melhorias, de três níveis cada:

| Melhoria | Efeito por nível |
| --- | --- |
| Resistência | Uma vida extra no começo da run |
| Kit inicial | Um vale para levar uma facilidade grátis da loja |
| Pechincha | 10% de desconto nos itens da loja |
| Refino | +5 pontos na fatia de energia que vira cristal |

O progresso é gravado no `localStorage`, em uma única chave (`triviaMaster.save`) com um objeto JSON versionado. Continua sem login, sem backend e sem banco de dados. Se o navegador bloquear o armazenamento local (janela anônima, por exemplo), o jogo avisa na tela de progressão e segue funcionando com o progresso valendo só enquanto a aba estiver aberta.

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
js/i18n.js       (textos da interface em PT e EN)
js/storage.js    (leitura e gravação do progresso permanente)
js/rogue.js      (modo roguelite: run, loja e melhorias)
js/app.js        (telas iniciais, modo clássico e roteamento)
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

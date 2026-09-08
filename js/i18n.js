const STRINGS = {
  pt: {
    appTitle: "Trivia Master",
    subtitle: "Teste seus conhecimentos de geografia, bandeiras, política e cultura",
    chooseCategory: "Escolha uma categoria",
    categories: {
      bandeiras: "Bandeiras",
      capitais: "Capitais",
      "politica-cultura": "Política & Cultura",
      todos: "Todos"
    },
    categoryDesc: {
      bandeiras: "Reconheça bandeiras de países do mundo todo",
      capitais: "Descubra capitais e seus respectivos países",
      "politica-cultura": "Fatos históricos, políticos e culturais",
      todos: "Perguntas de todas as categorias misturadas"
    },
    start: "Começar",
    questionOf: (n, total) => `Pergunta ${n} de ${total}`,
    score: "Pontuação",
    next: "Próxima",
    seeResult: "Ver resultado",
    correct: "Certo!",
    wrong: "Errado! A resposta certa é:",
    resultTitle: "Fim de jogo!",
    yourScore: (score, total) => `Você acertou ${score} de ${total}`,
    playAgain: "Jogar de novo",
    changeCategory: "Escolher outra categoria",
    messageGreat: "Excelente! Você manda bem nisso.",
    messageGood: "Nada mal! Continue praticando.",
    messageLow: "Continue estudando, você vai melhorar!",
    loading: "Carregando perguntas..."
  },
  en: {
    appTitle: "Trivia Master",
    subtitle: "Test your knowledge of geography, flags, politics and culture",
    chooseCategory: "Choose a category",
    categories: {
      bandeiras: "Flags",
      capitais: "Capitals",
      "politica-cultura": "Politics & Culture",
      todos: "All"
    },
    categoryDesc: {
      bandeiras: "Recognize flags from countries around the world",
      capitais: "Discover capitals and their countries",
      "politica-cultura": "Historical, political and cultural facts",
      todos: "Questions from every category mixed together"
    },
    start: "Start",
    questionOf: (n, total) => `Question ${n} of ${total}`,
    score: "Score",
    next: "Next",
    seeResult: "See result",
    correct: "Correct!",
    wrong: "Wrong! The correct answer is:",
    resultTitle: "Game over!",
    yourScore: (score, total) => `You got ${score} out of ${total}`,
    playAgain: "Play again",
    changeCategory: "Choose another category",
    messageGreat: "Excellent! You're great at this.",
    messageGood: "Not bad! Keep practicing.",
    messageLow: "Keep studying, you'll get better!",
    loading: "Loading questions..."
  }
};

const CATEGORY_ORDER = ["bandeiras", "capitais", "politica-cultura", "todos"];

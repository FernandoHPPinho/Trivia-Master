const ROUND_SIZE = 10;
const DATA_FILES = {
  bandeiras: "data/bandeiras.json",
  capitais: "data/capitais.json",
  "politica-cultura": "data/politica-cultura.json"
};

const state = {
  lang: "pt",
  data: {},
  category: null,
  round: [],
  index: 0,
  score: 0,
  answered: false,
  selectedIndex: null,
  screen: "home"
};

const app = document.getElementById("app");

function t() {
  return STRINGS[state.lang];
}

function shuffle(arr) {
  const copy = arr.slice();
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

async function loadData() {
  const entries = await Promise.all(
    Object.entries(DATA_FILES).map(async ([key, url]) => {
      const res = await fetch(url);
      const json = await res.json();
      return [key, json];
    })
  );
  entries.forEach(([key, json]) => {
    state.data[key] = json;
  });
}

function poolForCategory(category) {
  if (category === "todos") {
    return Object.values(state.data).flat();
  }
  return state.data[category] || [];
}

function setLang(lang) {
  state.lang = lang;
  const save = SaveStore.get();
  save.lang = lang;
  SaveStore.save();
  render();
}

function renderHeader() {
  const strings = t();
  return `
    <header class="app-header">
      <h1>${strings.appTitle}</h1>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button class="lang-btn ${state.lang === "pt" ? "active" : ""}" data-lang="pt">PT</button>
        <button class="lang-btn ${state.lang === "en" ? "active" : ""}" data-lang="en">EN</button>
      </div>
    </header>
  `;
}

// Ligar o seletor de idioma e a unica coisa que toda tela precisa repetir, entao
// vale um helper. Trocar de idioma so redesenha a tela atual, sem mexer no estado.
function bindLangButtons() {
  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.addEventListener("click", () => setLang(btn.dataset.lang));
  });
}

// Tela inicial: escolha entre os dois modos, que nao compartilham estado.
function renderHome() {
  state.screen = "home";
  const strings = t();
  const save = SaveStore.get();

  app.innerHTML = `
    ${renderHeader()}
    <main class="screen home-screen">
      <p class="subtitle">${strings.subtitle}</p>
      <h2 class="section-title">${strings.chooseMode}</h2>
      <div class="mode-grid">
        <button class="mode-card" id="mode-classic">
          <span class="category-icon">🎯</span>
          <span class="category-name">${strings.classicMode}</span>
          <span class="category-desc">${strings.classicModeDesc}</span>
          <span class="category-count">${strings.classicModeTag}</span>
        </button>
        <button class="mode-card mode-card-rogue" id="mode-rogue">
          <span class="category-icon">⚔️</span>
          <span class="category-name">${strings.rogueMode}</span>
          <span class="category-desc">${strings.rogueModeDesc}</span>
          <span class="category-count">${strings.rogueModeTag} · 💎 ${save.crystals}</span>
        </button>
      </div>
      <button class="secondary-btn" id="mode-upgrades">💎 ${strings.openUpgrades}</button>
    </main>
  `;

  bindLangButtons();
  document.getElementById("mode-classic").addEventListener("click", renderCategories);
  document.getElementById("mode-rogue").addEventListener("click", renderRogueIntro);
  document.getElementById("mode-upgrades").addEventListener("click", renderUpgrades);
}

// Tela de categorias do modo classico.
function renderCategories() {
  state.screen = "categories";
  const strings = t();
  const cards = CATEGORY_ORDER.map((cat) => {
    const pool = poolForCategory(cat);
    return `
      <button class="category-card" data-category="${cat}">
        <span class="category-icon">${categoryIcon(cat)}</span>
        <span class="category-name">${strings.categories[cat]}</span>
        <span class="category-desc">${strings.categoryDesc[cat]}</span>
        <span class="category-count">${pool.length}+ ${state.lang === "pt" ? "perguntas" : "questions"}</span>
      </button>
    `;
  }).join("");

  app.innerHTML = `
    ${renderHeader()}
    <main class="screen home-screen">
      <button class="link-btn" id="go-home">← ${strings.back}</button>
      <h2 class="section-title">${strings.chooseCategory}</h2>
      <div class="category-grid">${cards}</div>
    </main>
  `;

  bindLangButtons();
  document.getElementById("go-home").addEventListener("click", renderHome);

  document.querySelectorAll(".category-card").forEach((card) => {
    card.addEventListener("click", () => startGame(card.dataset.category));
  });
}

function categoryIcon(cat) {
  switch (cat) {
    case "bandeiras": return "🏳️";
    case "capitais": return "🏙️";
    case "politica-cultura": return "🏛️";
    case "todos": return "🌎";
    default: return "❓";
  }
}

function startGame(category) {
  state.category = category;
  const pool = poolForCategory(category);
  state.round = shuffle(pool).slice(0, ROUND_SIZE);
  state.index = 0;
  state.score = 0;
  state.screen = "question";
  state.selectedIndex = null;
  renderQuestion();
}

function renderQuestion() {
  state.screen = "question";
  const strings = t();
  const total = state.round.length;
  const question = state.round[state.index];
  const q = question[state.lang];
  const alreadyAnswered = state.selectedIndex !== null;

  const progressPct = Math.round((state.index / total) * 100);

  const optionsHtml = q.options.map((opt, i) => {
    let cls = "option-btn";
    if (alreadyAnswered) {
      cls += " disabled";
      if (i === question.answer) cls += " correct";
      if (i === state.selectedIndex && state.selectedIndex !== question.answer) cls += " wrong";
    }
    return `<button class="${cls}" data-index="${i}">${opt}</button>`;
  }).join("");

  let feedbackText = "";
  let feedbackClass = "";
  if (alreadyAnswered) {
    const isCorrect = state.selectedIndex === question.answer;
    feedbackText = isCorrect ? strings.correct : `${strings.wrong} ${q.options[question.answer]}`;
    feedbackClass = isCorrect ? "feedback-correct" : "feedback-wrong";
  }

  app.innerHTML = `
    ${renderHeader()}
    <main class="screen game-screen">
      <div class="game-meta">
        <span class="question-count">${strings.questionOf(state.index + 1, total)}</span>
        <span class="score-count">${strings.score}: ${state.score}</span>
      </div>
      <div class="progress-bar"><div class="progress-fill" style="width:${progressPct}%"></div></div>
      <h2 class="question-text">${q.question}</h2>
      <div class="options-grid">${optionsHtml}</div>
      <div class="feedback ${feedbackClass}" aria-live="polite">${feedbackText}</div>
      <button class="next-btn ${alreadyAnswered ? "" : "hidden"}">${state.index === total - 1 ? strings.seeResult : strings.next}</button>
    </main>
  `;

  bindLangButtons();

  document.querySelectorAll(".option-btn").forEach((btn) => {
    btn.addEventListener("click", () => selectOption(parseInt(btn.dataset.index, 10)));
  });

  document.querySelector(".next-btn").addEventListener("click", nextQuestion);
}

function selectOption(selectedIndex) {
  if (state.selectedIndex !== null) return;
  state.selectedIndex = selectedIndex;

  const question = state.round[state.index];
  const isCorrect = selectedIndex === question.answer;
  if (isCorrect) state.score += 1;

  renderQuestion();
}

function nextQuestion() {
  if (state.index < state.round.length - 1) {
    state.index += 1;
    state.selectedIndex = null;
    renderQuestion();
  } else {
    renderResult();
  }
}

function renderResult() {
  state.screen = "result";
  const strings = t();
  const total = state.round.length;
  const pct = total > 0 ? state.score / total : 0;
  let message = strings.messageLow;
  if (pct >= 0.8) message = strings.messageGreat;
  else if (pct >= 0.5) message = strings.messageGood;

  app.innerHTML = `
    ${renderHeader()}
    <main class="screen result-screen">
      <h2 class="result-title">${strings.resultTitle}</h2>
      <p class="result-score">${strings.yourScore(state.score, total)}</p>
      <p class="result-message">${message}</p>
      <div class="result-actions">
        <button class="primary-btn" id="play-again">${strings.playAgain}</button>
        <button class="secondary-btn" id="change-category">${strings.changeCategory}</button>
        <button class="link-btn" id="back-home">${strings.back}</button>
      </div>
    </main>
  `;

  bindLangButtons();

  document.getElementById("play-again").addEventListener("click", () => startGame(state.category));
  document.getElementById("change-category").addEventListener("click", renderCategories);
  document.getElementById("back-home").addEventListener("click", renderHome);
}

function render() {
  switch (state.screen) {
    case "categories":
      renderCategories();
      break;
    case "question":
      renderQuestion();
      break;
    case "result":
      renderResult();
      break;
    case "rogue-intro":
      renderRogueIntro();
      break;
    case "rogue-question":
      renderRogueQuestion();
      break;
    case "rogue-shop":
      renderRogueShop();
      break;
    case "rogue-over":
      renderRogueOver();
      break;
    case "upgrades":
      renderUpgrades();
      break;
    default:
      renderHome();
  }
}

async function init() {
  const save = SaveStore.get();
  state.lang = save.lang;
  app.innerHTML = `${renderHeader()}<main class="screen loading-screen"><p>${t().loading}</p></main>`;
  await loadData();
  renderHome();
}

init();

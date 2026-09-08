// Modo roguelite: sobrevivencia com vidas, loja de facilidades durante a run e
// progressao permanente entre partidas.
//
// Regra de ouro deste arquivo: nenhuma funcao de render pode alterar energia,
// vidas, cristais ou estatisticas. Toda mudanca de economia acontece dentro de um
// handler de clique. Assim, trocar de idioma ou redesenhar a tela nunca duplica
// recurso, do mesmo jeito que o campo selectedIndex protege o modo classico.

const ROGUE_BASE_LIVES = 3;
const ROGUE_STREAK_STEP = 3;        // a cada 3 acertos seguidos o bonus sobe 1
const ROGUE_STREAK_MAX_BONUS = 3;
const ROGUE_BASE_CONVERSION = 0.2;  // fatia da energia que vira cristal
const ROGUE_CONVERSION_STEP = 0.05; // ganho por nivel da melhoria de conversao
const ROGUE_PRICE_GROWTH = 0.5;     // o preco sobe 50% a cada compra na mesma run
const ROGUE_DISCOUNT_STEP = 0.1;    // desconto por nivel da melhoria de preco

// Itens da loja. "phase" diz quando o item faz sentido: "open" so vale enquanto a
// pergunta atual nao foi respondida, "any" vale a qualquer momento da run.
const ROGUE_ITEMS = [
  { id: "hint", icon: "🔍", base: 2, phase: "open" },
  { id: "fifty", icon: "✂️", base: 3, phase: "open" },
  { id: "skip", icon: "⏭️", base: 4, phase: "open" },
  { id: "shield", icon: "🛡️", base: 6, phase: "any" },
  { id: "heal", icon: "❤️", base: 8, phase: "any" }
];

// Melhorias permanentes. costs[i] e o preco em cristais para ir do nivel i para i+1.
const ROGUE_UPGRADES = [
  { id: "extraLife", icon: "🫀", costs: [8, 18, 32] },
  { id: "starterKit", icon: "🎁", costs: [10, 22, 40] },
  { id: "discount", icon: "🏷️", costs: [12, 25, 45] },
  { id: "conversion", icon: "💎", costs: [10, 20, 36] }
];

let run = null;

function rogueStrings() {
  return t().rogue;
}

function upgradeLevel(id) {
  return SaveStore.get().upgrades[id] || 0;
}

function upgradeCost(def) {
  const level = upgradeLevel(def.id);
  if (level >= def.costs.length) return null;
  return def.costs[level];
}

function rogueStartingLives() {
  return ROGUE_BASE_LIVES + upgradeLevel("extraLife");
}

function rogueConversionRate() {
  return ROGUE_BASE_CONVERSION + ROGUE_CONVERSION_STEP * upgradeLevel("conversion");
}

function rogueStreakBonus(streak) {
  return Math.min(Math.floor(streak / ROGUE_STREAK_STEP), ROGUE_STREAK_MAX_BONUS);
}

// O baralho da run mistura todas as categorias. E o que separa o roguelite do
// modo classico, onde a categoria e escolhida antes de comecar.
function rogueDeck() {
  return shuffle(poolForCategory("todos"));
}

function currentRogueQuestion() {
  return run.deck[run.cursor];
}

function rogueItemPrice(item) {
  const bought = run.purchases[item.id] || 0;
  const raw = Math.ceil(item.base * (1 + ROGUE_PRICE_GROWTH * bought));
  const discount = ROGUE_DISCOUNT_STEP * upgradeLevel("discount");
  return Math.max(1, Math.floor(raw * (1 - discount)));
}

function rogueItemAvailable(item) {
  if (!run || run.over) return false;
  const answered = run.selectedIndex !== null;
  if (item.phase === "open" && answered) return false;

  switch (item.id) {
    case "hint":
      return !run.hintUsed;
    case "fifty":
      return !run.fiftyUsed && currentRogueQuestion()[state.lang].options.length > 2;
    case "skip":
      return true;
    case "shield":
      return !run.shield;
    case "heal":
      return run.lives < run.maxLives;
    default:
      return false;
  }
}

// Bandeiras sao emoji formados por dois indicadores regionais, que juntos soletram
// o codigo do pais. Converter de volta para letras da uma pista util em alternativas
// que nao tem texto nenhum.
function flagCode(text) {
  let code = "";
  Array.from(text).forEach((ch) => {
    const cp = ch.codePointAt(0);
    if (cp >= 0x1f1e6 && cp <= 0x1f1ff) code += String.fromCharCode(65 + cp - 0x1f1e6);
  });
  return code;
}

function rogueHintText() {
  const question = currentRogueQuestion();
  const answer = String(question[state.lang].options[question.answer]).trim();
  // Array.from percorre por ponto de codigo, entao emoji contam como um caractere
  // so, em vez de virarem metade de um par substituto.
  const chars = Array.from(answer);
  const hasText = chars.some((ch) => /[\p{L}\p{N}]/u.test(ch));

  if (!hasText) {
    const code = flagCode(answer);
    if (code) return rogueStrings().hintFlag(code);
  }

  return rogueStrings().hintText(chars[0], chars.length);
}

function startRogueRun() {
  const deck = rogueDeck();
  const lives = rogueStartingLives();
  run = {
    deck: deck,
    cursor: 0,
    lives: lives,
    maxLives: lives,
    energy: 0,
    streak: 0,
    bestStreak: 0,
    correct: 0,
    answered: 0,
    vouchers: upgradeLevel("starterKit"),
    purchases: {},
    shield: false,
    // estado da pergunta atual
    selectedIndex: null,
    removed: [],
    hintUsed: false,
    fiftyUsed: false,
    shieldAbsorbed: false,
    lastGain: 0,
    // fim da run
    over: false,
    reward: 0
  };
  renderRogueQuestion();
}

function advanceRogueQuestion() {
  run.cursor += 1;
  if (run.cursor >= run.deck.length) {
    run.deck = rogueDeck();
    run.cursor = 0;
  }
  run.selectedIndex = null;
  run.removed = [];
  run.hintUsed = false;
  run.fiftyUsed = false;
  run.shieldAbsorbed = false;
  run.lastGain = 0;
}

function answerRogue(index) {
  if (!run || run.over) return;
  if (run.selectedIndex !== null) return;      // ja respondeu esta pergunta
  if (run.removed.indexOf(index) !== -1) return; // alternativa eliminada pelas cartas

  run.selectedIndex = index;
  run.answered += 1;

  const question = currentRogueQuestion();
  if (index === question.answer) {
    run.streak += 1;
    if (run.streak > run.bestStreak) run.bestStreak = run.streak;
    run.correct += 1;
    run.lastGain = 1 + rogueStreakBonus(run.streak);
    run.energy += run.lastGain;
  } else {
    run.streak = 0;
    run.lastGain = 0;
    if (run.shield) {
      run.shield = false;
      run.shieldAbsorbed = true;
    } else {
      run.lives -= 1;
    }
  }

  renderRogueQuestion();
}

function nextRogueQuestion() {
  if (!run || run.over) return;
  if (run.selectedIndex === null) return;
  if (run.lives <= 0) {
    endRogueRun();
    return;
  }
  advanceRogueQuestion();
  renderRogueQuestion();
}

// Converte a energia da run em cristais e grava o progresso. O guarda run.over faz
// isso acontecer uma unica vez: redesenhar a tela final nao premia de novo.
function endRogueRun() {
  if (!run || run.over) return;
  run.over = true;
  run.reward = Math.floor(run.energy * rogueConversionRate());

  const save = SaveStore.get();
  save.crystals += run.reward;
  save.stats.runs += 1;
  save.stats.totalCrystals += run.reward;
  if (run.correct > save.stats.bestCorrect) save.stats.bestCorrect = run.correct;
  if (run.bestStreak > save.stats.bestStreak) save.stats.bestStreak = run.bestStreak;
  SaveStore.save();

  renderRogueOver();
}

function buyRogueItem(id) {
  if (!run || run.over) return;
  const item = ROGUE_ITEMS.filter((entry) => entry.id === id)[0];
  if (!item || !rogueItemAvailable(item)) return;

  const usingVoucher = run.vouchers > 0;
  const price = usingVoucher ? 0 : rogueItemPrice(item);
  if (!usingVoucher && price > run.energy) return;

  if (usingVoucher) {
    run.vouchers -= 1;
  } else {
    run.energy -= price;
  }
  run.purchases[id] = (run.purchases[id] || 0) + 1;

  applyRogueItem(item);
}

function applyRogueItem(item) {
  const question = currentRogueQuestion();

  switch (item.id) {
    case "hint":
      run.hintUsed = true;
      renderRogueShop();
      break;
    case "fifty": {
      const wrong = [];
      question[state.lang].options.forEach((opt, i) => {
        if (i !== question.answer && run.removed.indexOf(i) === -1) wrong.push(i);
      });
      run.removed = run.removed.concat(shuffle(wrong).slice(0, 2));
      run.fiftyUsed = true;
      renderRogueShop();
      break;
    }
    case "skip":
      advanceRogueQuestion();
      renderRogueQuestion();
      break;
    case "shield":
      run.shield = true;
      renderRogueShop();
      break;
    case "heal":
      run.lives = Math.min(run.lives + 1, run.maxLives);
      renderRogueShop();
      break;
    default:
      renderRogueShop();
  }
}

function buyUpgrade(id) {
  const def = ROGUE_UPGRADES.filter((entry) => entry.id === id)[0];
  if (!def) return;
  const cost = upgradeCost(def);
  if (cost === null) return;

  const save = SaveStore.get();
  if (save.crystals < cost) return;

  save.crystals -= cost;
  save.upgrades[id] = upgradeLevel(id) + 1;
  SaveStore.save();

  renderUpgrades();
}

function resetProgress() {
  if (!window.confirm(rogueStrings().resetConfirm)) return;
  SaveStore.reset();
  renderUpgrades();
}

// ----- telas -----

function renderRogueHud() {
  const strings = rogueStrings();
  let hearts = "";
  for (let i = 0; i < run.maxLives; i++) {
    hearts += i < run.lives ? "❤️" : "🖤";
  }
  const shieldTag = run.shield
    ? `<span class="hud-chip hud-shield" title="${strings.shieldActive}">🛡️</span>`
    : "";

  return `
    <div class="rogue-hud">
      <span class="hud-chip hud-lives" aria-label="${strings.lives}">${hearts}</span>
      ${shieldTag}
      <span class="hud-chip">⚡ ${run.energy}</span>
      <span class="hud-chip">🔥 ${run.streak}</span>
      <span class="hud-chip">✅ ${run.correct}/${run.answered}</span>
    </div>
  `;
}

function renderRogueIntro() {
  state.screen = "rogue-intro";
  const strings = t();
  const rogue = strings.rogue;
  const save = SaveStore.get();
  const rules = rogue.rules.map((line) => `<li>${line}</li>`).join("");
  const vouchers = upgradeLevel("starterKit");

  app.innerHTML = `
    ${renderHeader()}
    <main class="screen rogue-intro-screen">
      <button class="link-btn" id="go-home">← ${strings.back}</button>
      <h2 class="section-title">${rogue.title}</h2>
      <p class="subtitle">${rogue.introLead}</p>
      <div class="info-card">
        <h3 class="info-title">${rogue.rulesTitle}</h3>
        <ul class="info-list">${rules}</ul>
      </div>
      <div class="stat-row">
        <span class="hud-chip">❤️ ${rogue.startingLives(rogueStartingLives())}</span>
        <span class="hud-chip">🎁 ${rogue.startingVouchers(vouchers)}</span>
        <span class="hud-chip">💎 ${rogue.balance(save.crystals)}</span>
      </div>
      <div class="result-actions">
        <button class="primary-btn" id="start-run">${rogue.startRun}</button>
        <button class="secondary-btn" id="go-upgrades">${strings.openUpgrades}</button>
      </div>
    </main>
  `;

  bindLangButtons();
  document.getElementById("go-home").addEventListener("click", renderHome);
  document.getElementById("start-run").addEventListener("click", startRogueRun);
  document.getElementById("go-upgrades").addEventListener("click", renderUpgrades);
}

function renderRogueQuestion() {
  if (!run) {
    renderRogueIntro();
    return;
  }
  state.screen = "rogue-question";
  const strings = t();
  const rogue = strings.rogue;
  const question = currentRogueQuestion();
  const q = question[state.lang];
  const answered = run.selectedIndex !== null;

  const optionsHtml = q.options.map((opt, i) => {
    let cls = "option-btn";
    if (run.removed.indexOf(i) !== -1) {
      cls += " disabled removed";
    } else if (answered) {
      cls += " disabled";
      if (i === question.answer) cls += " correct";
      if (i === run.selectedIndex && run.selectedIndex !== question.answer) cls += " wrong";
    }
    return `<button class="${cls}" data-index="${i}">${opt}</button>`;
  }).join("");

  let feedbackText = "";
  let feedbackClass = "";
  if (answered) {
    if (run.selectedIndex === question.answer) {
      feedbackClass = "feedback-correct";
      const bonus = rogueStreakBonus(run.streak);
      feedbackText = `${strings.correct} ${rogue.energyGain(run.lastGain)}`;
      if (bonus > 0) feedbackText += ` (${rogue.streakBonusNote(bonus)})`;
    } else {
      feedbackClass = "feedback-wrong";
      const tail = run.shieldAbsorbed ? rogue.shieldAbsorbed : rogue.lifeLost;
      feedbackText = `${strings.wrong} ${q.options[question.answer]} ${tail}`;
    }
  }

  const hintHtml = run.hintUsed
    ? `<p class="hint-box"><strong>${rogue.hintLabel}:</strong> ${rogueHintText()}</p>`
    : "";

  const nextLabel = run.lives <= 0 ? strings.seeResult : strings.next;

  app.innerHTML = `
    ${renderHeader()}
    <main class="screen game-screen">
      ${renderRogueHud()}
      <h2 class="question-text">${q.question}</h2>
      ${hintHtml}
      <div class="options-grid">${optionsHtml}</div>
      <div class="feedback ${feedbackClass}" aria-live="polite">${feedbackText}</div>
      <div class="result-actions">
        <button class="next-btn ${answered ? "" : "hidden"}" id="rogue-next">${nextLabel}</button>
        <button class="secondary-btn" id="open-shop">🛒 ${rogue.shopButton} (⚡ ${run.energy})</button>
      </div>
    </main>
  `;

  bindLangButtons();

  document.querySelectorAll(".option-btn").forEach((btn) => {
    btn.addEventListener("click", () => answerRogue(parseInt(btn.dataset.index, 10)));
  });

  document.getElementById("rogue-next").addEventListener("click", nextRogueQuestion);
  document.getElementById("open-shop").addEventListener("click", renderRogueShop);
}

function renderRogueShop() {
  if (!run || run.over) {
    renderRogueIntro();
    return;
  }
  state.screen = "rogue-shop";
  const strings = t();
  const rogue = strings.rogue;

  const cardsHtml = ROGUE_ITEMS.map((item) => {
    const info = rogue.items[item.id];
    const available = rogueItemAvailable(item);
    const usingVoucher = run.vouchers > 0;
    const price = rogueItemPrice(item);
    const affordable = usingVoucher || price <= run.energy;
    const enabled = available && affordable;

    let priceLabel = usingVoucher ? rogue.free : rogue.priceLabel(price);
    let note = "";
    if (!available) note = `<span class="shop-note">${rogue.notAvailable}</span>`;
    else if (!affordable) note = `<span class="shop-note">${rogue.notEnoughEnergy}</span>`;

    return `
      <div class="shop-card ${enabled ? "" : "shop-card-off"}">
        <span class="shop-icon">${item.icon}</span>
        <div class="shop-body">
          <span class="shop-name">${info.name}</span>
          <span class="shop-desc">${info.desc}</span>
          ${note}
        </div>
        <button class="shop-buy" data-item="${item.id}" ${enabled ? "" : "disabled"}>
          <span class="shop-price">${priceLabel}</span>
          <span>${rogue.buy}</span>
        </button>
      </div>
    `;
  }).join("");

  const voucherLine = run.vouchers > 0
    ? `<p class="shop-vouchers">🎁 ${rogue.vouchersLeft(run.vouchers)}</p>`
    : "";

  app.innerHTML = `
    ${renderHeader()}
    <main class="screen shop-screen">
      ${renderRogueHud()}
      <h2 class="section-title">${rogue.shopTitle}</h2>
      <p class="subtitle">${rogue.shopIntro}</p>
      ${voucherLine}
      <div class="shop-list">${cardsHtml}</div>
      <button class="primary-btn" id="close-shop">${rogue.backToQuestion}</button>
    </main>
  `;

  bindLangButtons();

  document.querySelectorAll(".shop-buy").forEach((btn) => {
    btn.addEventListener("click", () => buyRogueItem(btn.dataset.item));
  });

  document.getElementById("close-shop").addEventListener("click", renderRogueQuestion);
}

function renderRogueOver() {
  if (!run) {
    renderRogueIntro();
    return;
  }
  state.screen = "rogue-over";
  const strings = t();
  const rogue = strings.rogue;
  const save = SaveStore.get();

  const rewardLine = run.reward > 0
    ? rogue.overReward(run.reward)
    : rogue.overNoReward;

  app.innerHTML = `
    ${renderHeader()}
    <main class="screen result-screen">
      <h2 class="result-title">${rogue.overTitle}</h2>
      <p class="result-score">${rogue.overSummary(run.correct, run.answered)}</p>
      <p class="result-message">${rogue.overStreak(run.bestStreak)}</p>
      <div class="stat-row">
        <span class="hud-chip">⚡ ${rogue.overEnergy(run.energy)}</span>
        <span class="hud-chip">💎 ${rewardLine}</span>
      </div>
      <p class="result-message">${rogue.balance(save.crystals)}</p>
      <div class="result-actions">
        <button class="primary-btn" id="new-run">${rogue.newRun}</button>
        <button class="secondary-btn" id="go-upgrades">${rogue.goUpgrades}</button>
        <button class="secondary-btn" id="go-home">${rogue.goHome}</button>
      </div>
    </main>
  `;

  bindLangButtons();
  document.getElementById("new-run").addEventListener("click", startRogueRun);
  document.getElementById("go-upgrades").addEventListener("click", renderUpgrades);
  document.getElementById("go-home").addEventListener("click", renderHome);
}

function renderUpgrades() {
  state.screen = "upgrades";
  const strings = t();
  const rogue = strings.rogue;
  const save = SaveStore.get();

  const cardsHtml = ROGUE_UPGRADES.map((def) => {
    const info = rogue.upgrades[def.id];
    const level = upgradeLevel(def.id);
    const cost = upgradeCost(def);
    const maxed = cost === null;
    const affordable = !maxed && save.crystals >= cost;

    let pips = "";
    for (let i = 0; i < def.costs.length; i++) {
      pips += `<span class="pip ${i < level ? "pip-on" : ""}"></span>`;
    }

    let action;
    if (maxed) {
      action = `<span class="upgrade-max">${rogue.maxLevel}</span>`;
    } else {
      action = `
        <button class="shop-buy" data-upgrade="${def.id}" ${affordable ? "" : "disabled"}>
          <span class="shop-price">💎 ${rogue.costLabel(cost)}</span>
          <span>${rogue.upgrade}</span>
        </button>
      `;
    }

    const note = !maxed && !affordable
      ? `<span class="shop-note">${rogue.notEnoughCrystals}</span>`
      : "";

    return `
      <div class="shop-card ${maxed || affordable ? "" : "shop-card-off"}">
        <span class="shop-icon">${def.icon}</span>
        <div class="shop-body">
          <span class="shop-name">${info.name}</span>
          <span class="shop-desc">${info.desc}</span>
          <span class="upgrade-level">${rogue.levelOf(level, def.costs.length)}</span>
          <span class="pips">${pips}</span>
          ${note}
        </div>
        ${action}
      </div>
    `;
  }).join("");

  const warning = SaveStore.isPersistent()
    ? ""
    : `<p class="storage-warning">${rogue.storageWarning}</p>`;

  const pct = Math.round(rogueConversionRate() * 100);

  app.innerHTML = `
    ${renderHeader()}
    <main class="screen upgrades-screen">
      <button class="link-btn" id="go-home">← ${strings.back}</button>
      <h2 class="section-title">${rogue.upgradesTitle}</h2>
      <p class="subtitle">${rogue.upgradesIntro}</p>
      ${warning}
      <div class="stat-row">
        <span class="hud-chip">💎 ${rogue.balance(save.crystals)}</span>
        <span class="hud-chip">♻️ ${rogue.conversionRate(pct)}</span>
      </div>
      <div class="shop-list">${cardsHtml}</div>
      <h3 class="info-title">${rogue.statsTitle}</h3>
      <div class="stat-row">
        <span class="hud-chip">${rogue.statRuns}: ${save.stats.runs}</span>
        <span class="hud-chip">${rogue.statBestCorrect}: ${save.stats.bestCorrect}</span>
        <span class="hud-chip">${rogue.statBestStreak}: ${save.stats.bestStreak}</span>
        <span class="hud-chip">${rogue.statTotalCrystals}: ${save.stats.totalCrystals}</span>
      </div>
      <div class="result-actions">
        <button class="primary-btn" id="go-rogue">${rogue.title}</button>
        <button class="link-btn danger" id="reset-progress">${rogue.resetProgress}</button>
      </div>
    </main>
  `;

  bindLangButtons();

  document.querySelectorAll(".shop-buy[data-upgrade]").forEach((btn) => {
    btn.addEventListener("click", () => buyUpgrade(btn.dataset.upgrade));
  });

  document.getElementById("go-home").addEventListener("click", renderHome);
  document.getElementById("go-rogue").addEventListener("click", () => {
    if (run && !run.over) renderRogueQuestion();
    else renderRogueIntro();
  });
  document.getElementById("reset-progress").addEventListener("click", resetProgress);
}

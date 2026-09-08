// Persistencia do progresso permanente do modo roguelite.
//
// Tudo fica em uma unica chave do localStorage, guardando um objeto JSON com um
// campo "version". Isso deixa uma migracao futura simples: basta comparar a versao
// lida com SAVE_VERSION e converter, em vez de caçar varias chaves soltas.
//
// Se o localStorage nao estiver disponivel (navegacao anonima, cookies bloqueados,
// arquivo aberto direto do disco em alguns navegadores), o jogo continua funcionando
// com uma copia apenas em memoria, que se perde ao fechar a aba.

const SAVE_KEY = "triviaMaster.save";
const SAVE_VERSION = 1;

// Nivel maximo de qualquer melhoria permanente. Usado tambem para limitar valores
// lidos do disco, para que um save corrompido ou editado na mao nao quebre o jogo.
const UPGRADE_MAX_LEVEL = 3;
const UPGRADE_KEYS = ["extraLife", "starterKit", "discount", "conversion"];

const SaveStore = (function () {
  let cache = null;
  let available = null;
  let warned = false;

  function defaultSave() {
    const upgrades = {};
    UPGRADE_KEYS.forEach((key) => {
      upgrades[key] = 0;
    });
    return {
      version: SAVE_VERSION,
      crystals: 0,
      upgrades: upgrades,
      stats: {
        runs: 0,
        bestCorrect: 0,
        bestStreak: 0,
        totalCrystals: 0
      },
      lang: "pt"
    };
  }

  // Ler window.localStorage pode lancar excecao por si so em alguns navegadores,
  // entao o teste inteiro fica dentro do try.
  function isAvailable() {
    if (available !== null) return available;
    try {
      const probe = "triviaMaster.probe";
      window.localStorage.setItem(probe, "1");
      window.localStorage.removeItem(probe);
      available = true;
    } catch (err) {
      available = false;
    }
    return available;
  }

  function toCount(value, max) {
    const n = Math.floor(Number(value));
    if (!Number.isFinite(n) || n < 0) return 0;
    if (typeof max === "number" && n > max) return max;
    return n;
  }

  // Reconstroi o save a partir do que veio do disco, campo por campo, ignorando
  // qualquer coisa inesperada. O objeto devolvido tem sempre o formato completo.
  function sanitize(raw) {
    const clean = defaultSave();
    if (!raw || typeof raw !== "object") return clean;

    clean.crystals = toCount(raw.crystals);

    if (raw.upgrades && typeof raw.upgrades === "object") {
      UPGRADE_KEYS.forEach((key) => {
        clean.upgrades[key] = toCount(raw.upgrades[key], UPGRADE_MAX_LEVEL);
      });
    }

    if (raw.stats && typeof raw.stats === "object") {
      clean.stats.runs = toCount(raw.stats.runs);
      clean.stats.bestCorrect = toCount(raw.stats.bestCorrect);
      clean.stats.bestStreak = toCount(raw.stats.bestStreak);
      clean.stats.totalCrystals = toCount(raw.stats.totalCrystals);
    }

    if (raw.lang === "pt" || raw.lang === "en") {
      clean.lang = raw.lang;
    }

    return clean;
  }

  function migrate(raw) {
    if (!raw || typeof raw !== "object") return defaultSave();
    // Save de uma versao futura, gravado por uma versao mais nova do jogo.
    // Nao da para adivinhar o formato, entao comeca do zero em vez de quebrar.
    if (toCount(raw.version) > SAVE_VERSION) return defaultSave();
    // Versao 1 e a primeira, entao nao ha conversao a fazer ainda.
    return sanitize(raw);
  }

  function load() {
    if (cache) return cache;
    if (!isAvailable()) {
      cache = defaultSave();
      return cache;
    }
    try {
      const text = window.localStorage.getItem(SAVE_KEY);
      cache = text ? migrate(JSON.parse(text)) : defaultSave();
    } catch (err) {
      cache = defaultSave();
    }
    return cache;
  }

  function persist() {
    if (!cache) return false;
    cache.version = SAVE_VERSION;
    if (!isAvailable()) return false;
    try {
      window.localStorage.setItem(SAVE_KEY, JSON.stringify(cache));
      return true;
    } catch (err) {
      // Cota estourada ou permissao revogada no meio da sessao. O jogo segue com
      // a copia em memoria em vez de interromper a run.
      if (!warned) {
        warned = true;
        available = false;
      }
      return false;
    }
  }

  function reset() {
    cache = defaultSave();
    persist();
    return cache;
  }

  return {
    get: load,
    save: persist,
    reset: reset,
    isPersistent: isAvailable,
    maxLevel: UPGRADE_MAX_LEVEL,
    keys: UPGRADE_KEYS
  };
})();

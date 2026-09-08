# -*- coding: utf-8 -*-
import json
import random

random.seed(42)

with open("countries.json", encoding="utf-8") as f:
    countries = json.load(f)

def pick_distractors(pool, exclude_code, n=3):
    candidates = [c for c in pool if c["code"] != exclude_code]
    return random.sample(candidates, n)

flags_questions = []
capitals_questions = []

for i, c in enumerate(countries):
    others = pick_distractors(countries, c["code"])

    # --- FLAGS type A: show flag, choose country ---
    opts = [c] + others
    random.shuffle(opts)
    answer_idx = opts.index(c)
    flags_questions.append({
        "id": f"flag-a-{c['code']}",
        "category": "bandeiras",
        "pt": {
            "question": f"De qual país é esta bandeira: {c['flag']}?",
            "options": [o["pt"] for o in opts]
        },
        "en": {
            "question": f"Which country does this flag belong to: {c['flag']}?",
            "options": [o["en"] for o in opts]
        },
        "answer": answer_idx
    })

    # --- FLAGS type B: show country, choose flag ---
    opts2 = [c] + others
    random.shuffle(opts2)
    answer_idx2 = opts2.index(c)
    flags_questions.append({
        "id": f"flag-b-{c['code']}",
        "category": "bandeiras",
        "pt": {
            "question": f"Qual é a bandeira de {c['pt']}?",
            "options": [o["flag"] for o in opts2]
        },
        "en": {
            "question": f"Which flag belongs to {c['en']}?",
            "options": [o["flag"] for o in opts2]
        },
        "answer": answer_idx2
    })

    # --- CAPITALS type A: given country, choose capital ---
    others_cap = pick_distractors(countries, c["code"])
    opts3 = [c] + others_cap
    random.shuffle(opts3)
    answer_idx3 = opts3.index(c)
    capitals_questions.append({
        "id": f"cap-a-{c['code']}",
        "category": "capitais",
        "pt": {
            "question": f"Qual é a capital de {c['pt']}?",
            "options": [o["capitalPt"] for o in opts3]
        },
        "en": {
            "question": f"What is the capital of {c['en']}?",
            "options": [o["capitalEn"] for o in opts3]
        },
        "answer": answer_idx3
    })

    # --- CAPITALS type B: given capital, choose country ---
    others_cap2 = pick_distractors(countries, c["code"])
    opts4 = [c] + others_cap2
    random.shuffle(opts4)
    answer_idx4 = opts4.index(c)
    capitals_questions.append({
        "id": f"cap-b-{c['code']}",
        "category": "capitais",
        "pt": {
            "question": f"{c['capitalPt']} é a capital de qual país?",
            "options": [o["pt"] for o in opts4]
        },
        "en": {
            "question": f"{c['capitalEn']} is the capital of which country?",
            "options": [o["en"] for o in opts4]
        },
        "answer": answer_idx4
    })

with open("../data/bandeiras.json", "w", encoding="utf-8") as f:
    json.dump(flags_questions, f, ensure_ascii=False, indent=2)

with open("../data/capitais.json", "w", encoding="utf-8") as f:
    json.dump(capitals_questions, f, ensure_ascii=False, indent=2)

print("flags:", len(flags_questions))
print("capitals:", len(capitals_questions))

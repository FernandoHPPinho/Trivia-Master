# -*- coding: utf-8 -*-
import json

files = ["../data/bandeiras.json", "../data/capitais.json", "../data/politica-cultura.json"]
total = 0
errors = []
ids = set()

for fname in files:
    with open(fname, encoding="utf-8") as f:
        data = json.load(f)
    total += len(data)
    for item in data:
        qid = item.get("id")
        if qid in ids:
            errors.append(f"{fname}: duplicate id {qid}")
        ids.add(qid)

        for lang in ("pt", "en"):
            block = item.get(lang)
            if not block:
                errors.append(f"{fname}/{qid}: missing {lang} block")
                continue
            opts = block.get("options")
            if not opts or len(opts) != 4:
                errors.append(f"{fname}/{qid}: {lang} options count != 4 ({opts})")
            if len(set(opts)) != len(opts):
                errors.append(f"{fname}/{qid}: {lang} duplicate options {opts}")
            if not block.get("question"):
                errors.append(f"{fname}/{qid}: {lang} missing question text")

        ans = item.get("answer")
        if ans is None or not (0 <= ans <= 3):
            errors.append(f"{fname}/{qid}: invalid answer index {ans}")

print("total questions:", total)
print("unique ids:", len(ids))
print("errors found:", len(errors))
for e in errors[:50]:
    print(" -", e)

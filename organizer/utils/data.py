import json

with open("rules.json", "r") as f:
    rules = json.load(f)

with open("undo.json", "r") as w:
    history = json.load(w)

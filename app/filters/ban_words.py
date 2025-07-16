import json
from pathlib import Path

Helper = Path(__file__).resolve().parent
Words_Path = Helper / "words.json"

with open(Words_Path, "r", encoding="utf-8") as f:
    data = json.load(f)
    BANWORDS = data["BANWORDS"]

def container_words(text: str) -> bool:
    return any(w in text.lower() for w in BANWORDS)


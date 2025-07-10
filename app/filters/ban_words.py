# for test
BANWORDS = ["путин", "украина", "политика", "война"]

def container_words(text: str) -> bool:
    return any(w in text.lower() for w in BANWORDS)
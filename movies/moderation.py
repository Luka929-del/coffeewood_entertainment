BANNED_WORDS = [
    "idiot", "stupid", "hate", "kill", "fuck", "shit",
    "bitch", "asshole", "damn", "dumb", "crap", "moron",
    "suck", "loser", "trash", "fool", "jerk", "bollocks",
    "dick", "piss", "cock", "bastard", "slut", "whore",
    "nazi", "racist", "terrorist", "bomb", "rape"
]


def contains_banned_words(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in BANNED_WORDS)

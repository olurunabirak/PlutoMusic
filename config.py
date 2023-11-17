from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6845799926"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("BAAhIHQAe4R2vE3QS9D77f9C1Z9xRff3gCo4tTf3ESrMB3Qpo1EdhKIryEHYcxisvdXCPFRE4lwEwlmP6qRO5Pm413i-OPF1KjfHRohZrGxAzouuF46TfrXO8Z11uEW8uPGcfBFraGix-J_4V9CoIpcMbBUyFwyCZ7xQfl0W_snd665-2o3JtifW3aaL7PsPKKJTQGQ0FvkD2eTk9cmltP0gCxhHGvUKUt9aW1c_J0mItquEXNTWUJkc2Dj6lPKpdeHMclYeCZy1Kblgstb3FJGtJ_02dsjAJhFz65WZHkXCy6rxuviCeR0aNKi9ZcRlBwh2CzVEPDoVQJ2LWviUFj1IsKbiuQAAAAGYCp32AA", None)

SUPPORT_CHAT = getenv("https://t.me/zirve_chat", "https://t.me/destekgroup")
SUPPORT_CHANNEL = getenv("https://t.me/zirve_chat", "https://t.me/PlutoKanal")
PLAYLIST = getenv("https://t.me/sendnedr", "https://t.me/PlutoFm")

PLAYLIST_ID = int(getenv("-1001995892657", ""))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

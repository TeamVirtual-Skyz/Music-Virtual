from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","🧸ᴍᴜꜱɪᴄ ᴠɪʀᴛᴜᴀʟ🧸")
BOT_USERNAME = getenv("BOT_USERNAME", "MusicCtvBot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "FvckMiaw")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Grup_Cari_Teman_Virtual")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/0ad42a2620eebf7e49510.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/cf9661d91b5dcecc7bf96.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))

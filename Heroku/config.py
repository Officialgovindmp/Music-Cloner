from os import getenv
from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
CLONER_TOKEN = getenv("CLONER_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSID = int(getenv("ASSID"))
ASSNAME = getenv("ASSNAME")
ASSUSERNAME = getenv("ASSUSERNAME")
BOT_ID = int(getenv("BOT_ID"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID"))
UPDATE = getenv("UPDATE", "@GOVIND_USERBOT_SPPORT")
SUPPORT = getenv("SUPPORT", "fwf_world")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://te.legra.ph/file/24c30c36586279cce847d.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6092973716").split()))
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/24c30c36586279cce847d.jpg")
OWNER_USERNAME = getenv("OWNER_USERNAME")
IMG_1 = "https://te.legra.ph/file/24c30c36586279cce847d.jpg"

import re
from os import environ, getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Log channel handling
log_channel = environ.get('LOG_CHANNEL', '')
LOG_CHANNEL = int(log_channel) if log_channel and id_pattern.search(log_channel) else None

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/65fe86fc02a73f6fcf0ce.jpg https://telegra.ph/file/6fa70325813885809a64a.jpg https://telegra.ph/file/e06afc1e7abbcd8d4213a.jpg https://telegra.ph/file/3f4040b320d9b7840200a.jpg https://telegra.ph/file/3950fad740fb8ea894df7.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/85d361ab4cb6511006022.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/86b7b7e2aa7e38f328902.jpg")
SUBSCRIPTION = environ.get('SUBSCRIPTION', 'https://telegra.ph/file/734170f40b8169830d821.jpg')
CODE = environ.get('CODE', 'https://telegra.ph/file/72f425007b22d28bd935e.jpg')

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Additional settings
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'instantearn.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '1502a197c85d59929d50f1cba1d5e6f967d1e962')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))

# Logging
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', ''))

LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing IMDb details for your queries.\n" if is_enabled(environ.get('IMDB', "False"), False) else "IMDb Results are disabled.\n")
LOG_STR += ("Single Button Mode enabled, filename and file size will be shown in a single button instead of two separate buttons\n" if is_enabled(environ.get('SINGLE_BUTTON', "True"), True) else "Single Button Mode disabled.\n")
LOG_STR += (f"Custom File Caption enabled with value {environ.get('CUSTOM_FILE_CAPTION', f'{script.CAPTION}')}, files will be sent with this customized caption.\n" if environ.get('CUSTOM_FILE_CAPTION') else "No Custom File Caption found, default captions will be used.\n")
LOG_STR += ("Spell Check Mode Enabled, bot will suggest related movies if a movie is not found\n" if is_enabled(environ.get('SPELL_CHECK_REPLY', "True"), True) else "Spell Check Mode disabled.\n")
LOG_STR += f"Your current IMDb template is {environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')}.\n"

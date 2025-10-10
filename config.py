#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "22413321")
API_HASH = os.environ.get("API_HASH", "19dc6a4da93120d1af60afd778559d55")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7766638158:AAHj5jPc2PhiNUS4UiXooRrMLRSp833YSMo")
ADMIN = int(os.environ.get("ADMIN", '2052400282'))
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://envs.sh/EMq.jpeg" # Replace with your Telegraph link - Start Pic
INFO_PIC= "https://envs.sh/EM0.jpg" # Replace with your Telegraph link - Information 
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "https://t.me/multibotvi") # Replace with your Updates link
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/compressbotlogs1") # Replace with your Support link
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8081")) #for koyeb 8080 only

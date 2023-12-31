# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "API_ID"))
API_HASH = os.environ.get("API_HASH", "API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "BOT_TOKEN")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "ADMINS").split(",") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "False"

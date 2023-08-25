# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "18522520"))
API_HASH = os.environ.get("API_HASH", "7ae9da3e228f89c1557d3d6de9e635b3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6568201991:AAF3j-weeNbXh7YpfycHAOSqZqHtvacEITI")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "5868126738").split(",") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Bishalghale:Bishalghale@cluster0.z7gtude.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5868126738")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001528714984")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Kajilinks_Official") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "False"

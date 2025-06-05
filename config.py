from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "27383453"))
API_HASH = getenv("API_HASH", "4c246fb0c649477cc2e79b6a178ddfaa")

BOT_TOKEN = getenv("BOT_TOKEN", "8172060393:AAHus9ttkV5LARaLn9MhM7f_rzZ3WVHIZog")
OWNER_ID = int(getenv("OWNER_ID", "8181241262"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sujoy123m:wTWKGUaxYE7dxb1l@cluster0.zorxb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "ProToppers")

import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [
    469203207,
    466080623,
    487868221,
    1093530249,
    1115993235,
    5031186929,
    1469224518,
    537683865
]

time_zone = 1

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

DATABASE = str(os.getenv("DATABASE"))

DB_USER = str(os.getenv("DB_USER"))
DB_PASS = str(os.getenv("DB_PASS"))
DB_HOST = str(os.getenv("DB_HOST"))

POSTGRES_URL = f'postgresql://{DB_USER}:{DB_PASS}@{ip}/{DATABASE}'

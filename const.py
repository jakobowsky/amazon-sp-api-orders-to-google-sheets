import os
from dotenv import load_dotenv

load_dotenv()

REFRESH_TOKEN = os.environ["REFRESH_TOKEN"]
LWA_APP_ID = os.environ["LWA_APP_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
AWS_ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
AWS_SECRET_KEY = os.environ["AWS_SECRET_KEY"]
ROLE_ARN = os.environ["ROLE_ARN"]

GOOGLE_SHEETS_EMAIL = os.environ["GOOGLE_SHEETS_EMAIL"]
GOOGLE_SHEETS_ID = os.environ["GOOGLE_SHEETS_ID"]
GOOGLE_WORKSHEET_NAME = os.environ["GOOGLE_WORKSHEET_NAME"]

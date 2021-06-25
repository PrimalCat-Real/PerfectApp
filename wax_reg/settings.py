import os
import dotenv

dotenv.load_dotenv('.env')

API_KEY = os.environ["api_key_anticaptcha"]
SITE_KEY = os.environ["site_key_wax"]
PROTON_NAME = os.environ["proton_name"]
PROTON_PASSWORD = os.environ["proton_password"]
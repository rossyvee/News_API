from dotenv import dotenv_values

config = dotenv_values(".env")

API_KEY = config.get("API_KEY")
NEWS_BASE_URL = config.get("NEWS_BASE_URL")

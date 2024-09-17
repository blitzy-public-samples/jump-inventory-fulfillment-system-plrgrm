from os import getenv
from dotenv import load_dotenv

# Global variables
SHOPIFY_API_KEY = getenv('SHOPIFY_API_KEY')
SHOPIFY_API_SECRET = getenv('SHOPIFY_API_SECRET')
SENDLE_API_KEY = getenv('SENDLE_API_KEY')
DATABASE_URL = getenv('DATABASE_URL')
REDIS_URL = getenv('REDIS_URL')
JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
GOOGLE_CLOUD_PROJECT = getenv('GOOGLE_CLOUD_PROJECT')

def load_config():
    """
    Loads configuration from environment variables
    """
    load_dotenv()  # Load environment variables from .env file
    
    global SHOPIFY_API_KEY, SHOPIFY_API_SECRET, SENDLE_API_KEY, DATABASE_URL, REDIS_URL, JWT_SECRET_KEY, GOOGLE_CLOUD_PROJECT
    
    SHOPIFY_API_KEY = getenv('SHOPIFY_API_KEY')
    SHOPIFY_API_SECRET = getenv('SHOPIFY_API_SECRET')
    SENDLE_API_KEY = getenv('SENDLE_API_KEY')
    DATABASE_URL = getenv('DATABASE_URL')
    REDIS_URL = getenv('REDIS_URL')
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
    GOOGLE_CLOUD_PROJECT = getenv('GOOGLE_CLOUD_PROJECT')
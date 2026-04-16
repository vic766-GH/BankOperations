from dotenv import load_dotenv
import os

    # Load environment variables from 111.env file
load_dotenv()

    # Access environment variables
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
debug = os.getenv('DEBUG')

try:
    import dotenv
    print("python-dotenv is installed successfully!")
except ImportError:
    print("python-dotenv is not installed.")

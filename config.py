import os 
from dotenv import load_dotenv

# load the .env file
load_dotenv()

ROOT_DIR = os.path.abspath(os.curdir)
SQL_USER=os.getenv("SQL_USER")
SQL_PWD=os.getenv("SQL_PWD")
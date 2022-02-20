import os
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
STATIC_FILES_DIR = os.path.join(ROOT_DIR, 'static')
STATIC_URL = '/static/'
DB_PATH = os.path.join(ROOT_DIR, 'testDB.sqlite3')

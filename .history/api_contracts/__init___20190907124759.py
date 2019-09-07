"""Contract tests for api testing."""
from pathlib import Path

from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(verbose=True, dotenv_path=env_path)

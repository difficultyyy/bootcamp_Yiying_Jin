from typing import Optional
import sys
import os

try:
    from dotenv import load_dotenv
    print("Imports OK")
except Exception as e:
    print("Import error:", e)
    raise


def load_env():
    load_dotenv()


def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

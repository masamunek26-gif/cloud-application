import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.config import settings

def configured(value) -> str:
    return "CONFIGURED" if value.get_secret_value() else "EMPTY"

def main():
    print("LAB_DB_PASSWORD:", configured(settings.lab_db_password))
    print("AUTH_SECRET:", configured(settings.auth_secret))
    
    key_path = Path(settings.ssl_keyfile) if settings.ssl_keyfile else None
    print("TLS_PRIVATE_KEY:", "EXISTS" if key_path and key_path.exists() else "MISSING")

if __name__ == "__main__":
    main()
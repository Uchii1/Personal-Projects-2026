import sqlite3
from datetime import date
from pathlib import Path

base = Path(r"C:\Users\uchec\studySoft")
backup_dir = base / "backups"
backup_dir.mkdir(exist_ok=True)

src = sqlite3.connect(base / "db.sqlite3")
dst = sqlite3.connect(backup_dir / f"db_{date.today()}.db")
src.backup(dst)
dst.close()
src.close()
print("Backup done")
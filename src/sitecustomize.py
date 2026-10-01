from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "backend" / "app" / "paper.py"
DB = ROOT / "backend" / "app" / "db.py"

try:
    if PAPER.exists():
        s = PAPER.read_text()
        old = "INSERT INTO positions("
        if old in s:
            PAPER.write_text(s.replace(old, "INSERT OR IGNORE INTO positions(", 1))

    if DB.exists():
        s = DB.read_text()
        old = "sqlite3.connect(DB_PATH)"
        if old in s and "sqlite3.connect(DB_PATH, timeout=30)" not in s:
            DB.write_text(s.replace(old, "sqlite3.connect(DB_PATH, timeout=30)", 1))

    print("[V50 HOTFIX] SQLite patch applied")
except Exception as exc:
    print(f"[V50 HOTFIX] patch failed: {exc}")

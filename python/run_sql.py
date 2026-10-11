"""Execute one SELECT/WITH query file; output CSV to stdout. Run from repo root."""
import csv, sqlite3, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
if len(sys.argv) != 2:
    raise SystemExit("Usage: python python/run_sql.py sql/00_profile.sql")
db = sqlite3.connect(root / "work/analytics.sqlite")
cur = db.execute(Path(sys.argv[1]).read_text())
w = csv.writer(sys.stdout)
w.writerow([x[0] for x in cur.description])
w.writerows(cur.fetchall())
db.close()

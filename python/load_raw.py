"""Run from repository root. Keeps raw fields as TEXT; requires Python stdlib only."""
from pathlib import Path
import csv, sqlite3

root = Path(__file__).resolve().parents[1]
(root / "work").mkdir(exist_ok=True)
db = sqlite3.connect(root / "work/analytics.sqlite")
for path in sorted((root / "data/raw").glob("*.csv")):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames
        rows = [tuple(row[c] for c in columns) for row in reader]
    name = "raw_" + path.stem
    db.execute(f'DROP TABLE IF EXISTS "{name}"')
    db.execute(f'CREATE TABLE "{name}" (' + ",".join(f'"{c}" TEXT' for c in columns) + ")")
    db.executemany(f'INSERT INTO "{name}" VALUES (' + ",".join("?" for _ in columns) + ")", rows)
    print(name, len(rows))
db.commit()
db.close()

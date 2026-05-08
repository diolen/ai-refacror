import sqlite3

conn = sqlite3.connect("memory.db")
c = conn.cursor()


def column_exists(table, column):
    c.execute(f"PRAGMA table_info({table})")
    cols = [row[1] for row in c.fetchall()]
    return column in cols


# changes table migrations
if not column_exists("changes", "summary"):
    c.execute("ALTER TABLE changes ADD COLUMN summary TEXT")

if not column_exists("changes", "reason"):
    c.execute("ALTER TABLE changes ADD COLUMN reason TEXT")


# create memory table
c.execute("""
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    type TEXT,
    text TEXT,
    confidence REAL
)
""")

conn.commit()
conn.close()

print("Migration complete")
import sqlite3

conn = sqlite3.connect("memory.db")
c = conn.cursor()


def column_exists(table, column):

    c.execute(f"PRAGMA table_info({table})")

    cols = [row[1] for row in c.fetchall()]

    return column in cols


# =========================
# CHANGES
# =========================
c.execute("""
CREATE TABLE IF NOT EXISTS changes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    file TEXT,
    function TEXT,
    prompt TEXT,
    model TEXT,
    input_code TEXT,
    output_code TEXT,
    status TEXT
)
""")


if not column_exists("changes", "summary"):
    c.execute("ALTER TABLE changes ADD COLUMN summary TEXT")

if not column_exists("changes", "reason"):
    c.execute("ALTER TABLE changes ADD COLUMN reason TEXT")


# =========================
# MEMORY
# =========================
c.execute("""
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    type TEXT,
    text TEXT,
    confidence REAL,
    UNIQUE(type, text)
)
""")


# =========================
# SNAPSHOTS
# =========================
c.execute("""
CREATE TABLE IF NOT EXISTS snapshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    name TEXT,
    data TEXT
)
""")


conn.commit()
conn.close()

print("Migration complete")
import sqlite3

conn = sqlite3.connect("memory.db")
c = conn.cursor()

# changes table
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
    status TEXT,
    summary TEXT,
    reason TEXT
)
""")

# memory table
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

print("DB initialized")
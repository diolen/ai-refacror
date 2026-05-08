import sqlite3

conn = sqlite3.connect("memory.db")
c = conn.cursor()

c.execute("""
    DELETE FROM memory
    WHERE text LIKE '%Auth%'
""")

conn.commit()
conn.close()

print("Cleanup complete")
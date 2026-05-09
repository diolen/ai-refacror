import sqlite3

DB_PATH = "memory.db"


# =========================
# LAST MEMORY EVENTS
# =========================
def show_last(limit=10):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT
            id,
            timestamp,
            type,
            text,
            confidence
        FROM memory
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = c.fetchall()

    for r in rows:
        print("\n---")
        print(f"ID: {r[0]}")
        print(f"Time: {r[1]}")
        print(f"Type: {r[2]}")
        print(f"Text: {r[3]}")
        print(f"Confidence: {r[4]}")

    conn.close()


# =========================
# MEMORY SEARCH
# =========================
def search(keyword):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT
            id,
            timestamp,
            type,
            text,
            confidence
        FROM memory
        WHERE
            text LIKE ?
            OR type LIKE ?
        ORDER BY id DESC
    """, (
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    rows = c.fetchall()

    for r in rows:
        print("\n---")
        print(f"ID: {r[0]}")
        print(f"Time: {r[1]}")
        print(f"Type: {r[2]}")
        print(f"Text: {r[3]}")
        print(f"Confidence: {r[4]}")

    conn.close()


# =========================
# RAW MEMORY VIEW
# =========================
def show_memory(limit=20):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT
            id,
            timestamp,
            type,
            text,
            confidence
        FROM memory
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = c.fetchall()

    for r in rows:
        print("\n---")
        print(f"ID: {r[0]}")
        print(f"Time: {r[1]}")
        print(f"Type: {r[2]}")
        print(f"Text: {r[3]}")
        print(f"Confidence: {r[4]}")

    conn.close()


# =========================
# TIMELINE
# =========================
def show_timeline():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT
            id,
            timestamp,
            type,
            text
        FROM memory
        ORDER BY id ASC
    """)

    rows = c.fetchall()

    current_day = None

    for r in rows:

        day = r[1][:10]

        if day != current_day:
            current_day = day
            print(f"\n=== {day} ===")

        print(f"[{r[2]}] {r[3]}")

    conn.close()
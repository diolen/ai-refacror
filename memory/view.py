import sqlite3

DB_PATH = "memory.db"


def show_last(limit=10):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT
            id,
            timestamp,
            file,
            function,
            summary,
            reason
        FROM changes
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = c.fetchall()

    for r in rows:
        print("\n---")
        print(f"ID: {r[0]}")
        print(f"Time: {r[1]}")
        print(f"File: {r[2]}")
        print(f"Function: {r[3]}")
        print(f"Summary: {r[4]}")
        print(f"Reason: {r[5]}")

    conn.close()


def search(keyword):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT
            id,
            timestamp,
            file,
            function,
            summary
        FROM changes
        WHERE
            file LIKE ?
            OR function LIKE ?
            OR summary LIKE ?
        ORDER BY id DESC
    """, (
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    rows = c.fetchall()

    for r in rows:
        print("\n---")
        print(f"ID: {r[0]}")
        print(f"Time: {r[1]}")
        print(f"File: {r[2]}")
        print(f"Function: {r[3]}")
        print(f"Summary: {r[4]}")

    conn.close()


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


def show_timeline():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT
            timestamp,
            type,
            text
        FROM memory
        ORDER BY timestamp ASC
    """)

    rows = c.fetchall()

    current_day = None

    for r in rows:
        day = r[0][:10]

        if day != current_day:
            current_day = day
            print(f"\n=== {day} ===")

        print(f"[{r[1]}] {r[2]}")

    conn.close()
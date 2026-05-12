import sqlite3
import datetime
import json

DB_PATH = "memory.db"


# =========================
# CHANGES LOG
# =========================
def save_change(
    file,
    function,
    prompt,
    model,
    input_code,
    output_code,
    status,
    summary="",
    reason=""
):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT INTO changes (
            timestamp,
            file,
            function,
            prompt,
            model,
            input_code,
            output_code,
            status,
            summary,
            reason
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.datetime.now().isoformat(),
        file,
        function,
        prompt,
        model,
        input_code,
        output_code,
        status,
        summary,
        reason
    ))

    conn.commit()
    conn.close()


# =========================
# MEMORY
# =========================
def save_memory(entry):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT OR IGNORE INTO memory (
            timestamp,
            type,
            text,
            confidence
        )
        VALUES (?, ?, ?, ?)
    """, (
        datetime.datetime.now().isoformat(),
        entry["type"],
        entry["text"],
        entry.get("confidence", 1.0)
    ))

    conn.commit()
    conn.close()


# =========================
# SNAPSHOTS
# =========================
def save_snapshot(name, data):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT INTO snapshots (
            timestamp,
            name,
            data
        )
        VALUES (?, ?, ?)
    """, (
        datetime.datetime.now().isoformat(),
        name,
        json.dumps(data, ensure_ascii=False, indent=2)
    ))

    conn.commit()
    conn.close()


def load_snapshot(name):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT data
        FROM snapshots
        WHERE name = ?
        ORDER BY id DESC
        LIMIT 1
    """, (name,))

    row = c.fetchone()

    conn.close()

    if not row:
        return None

    return json.loads(row[0])


def list_snapshots():

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT id, timestamp, name
        FROM snapshots
        ORDER BY id DESC
    """)

    rows = c.fetchall()

    conn.close()

    return rows


# =========================
# WRAPPERS
# =========================
def save_milestone(text):

    save_memory({
        "type": "milestone",
        "text": text,
        "confidence": 1.0
    })


def save_decision(text):

    save_memory({
        "type": "decision",
        "text": text,
        "confidence": 1.0
    })


def save_insight(text, confidence=0.8):

    save_memory({
        "type": "insight",
        "text": text,
        "confidence": confidence
    })


# =========================
# UTILITY
# =========================
def memory_exists(text, type_):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT 1
        FROM memory
        WHERE text = ? AND type = ?
        LIMIT 1
    """, (text, type_))

    row = c.fetchone()

    conn.close()

    return row is not None
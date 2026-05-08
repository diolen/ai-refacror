import sqlite3
import datetime

DB_PATH = "memory.db"


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


def save_memory(entry):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT INTO memory (
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

def memory_exists(text, type_):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT id
        FROM memory
        WHERE text = ? AND type = ?
        LIMIT 1
    """, (text, type_))

    row = c.fetchone()

    conn.close()

    return row is not None
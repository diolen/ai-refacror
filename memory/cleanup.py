import sqlite3
import argparse

DB_PATH = "memory.db"


def cleanup_memory(keyword=None, type_=None, wipe_all=False):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if wipe_all:
        confirm = input("WARNING: delete ALL memory? (yes/no): ")
        if confirm.lower() != "yes":
            print("Aborted")
            return

        c.execute("DELETE FROM memory")
        conn.commit()
        conn.close()

        print("ALL memory deleted")
        return

    query = "DELETE FROM memory WHERE 1=1"
    params = []

    if keyword:
        query += " AND text LIKE ?"
        params.append(f"%{keyword}%")

    if type_:
        query += " AND type = ?"
        params.append(type_)

    c.execute(query, params)

    conn.commit()
    conn.close()

    print("Cleanup complete")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--keyword")
    parser.add_argument("--type")
    parser.add_argument("--wipe-all", action="store_true")

    args = parser.parse_args()

    cleanup_memory(
        keyword=args.keyword,
        type_=args.type,
        wipe_all=args.wipe_all
    )
import json

from memory.db import (
    save_snapshot,
    load_snapshot,
    list_snapshots
)


# =========================
# CREATE SNAPSHOT
# =========================
def create_snapshot(name, entity_model):

    save_snapshot(name, entity_model)

    print(f"[snapshot] saved: {name}")

    return 0


# =========================
# SHOW SNAPSHOT
# =========================
def show_snapshot(name):

    snapshot = load_snapshot(name)

    if snapshot is None:
        print(f"Snapshot not found: {name}")
        return 1

    print(json.dumps(snapshot, indent=2, ensure_ascii=False))

    return 0


# =========================
# LIST SNAPSHOTS
# =========================
def show_snapshots():

    rows = list_snapshots()

    if not rows:
        print("No snapshots")
        return 0

    print("\nSNAPSHOTS\n")

    for row in rows:

        snapshot_id, timestamp, name = row

        print(f"[{snapshot_id}] {timestamp} :: {name}")

    return 0
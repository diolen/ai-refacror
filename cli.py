import argparse

from analysis.adapters.cakephp2.runner import (
    run_scan,
    run_impact,
    run_merge,
    run_prompt,
    build_runtime_entity_model
)

from memory.view import (
    show_last,
    show_memory,
    show_timeline,
    search
)

from memory.snapshot import (
    create_snapshot,
    show_snapshot,
    show_snapshots
)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--adapter",
        choices=["cakephp2", "cakephp3", "cakephp4"],
        default="cakephp2"
    )

    sub = parser.add_subparsers(dest="command")

    # =========================
    # SCAN
    # =========================
    scan = sub.add_parser("scan")

    scan.add_argument("file")

    scan.add_argument(
        "--adapter",
        choices=["cakephp2", "cakephp3", "cakephp4"],
        default="cakephp2"
    )

    # =========================
    # IMPACT
    # =========================
    impact = sub.add_parser("impact")

    impact.add_argument("entity")
    impact.add_argument("controller")
    impact.add_argument("model")

    impact.add_argument(
        "--adapter",
        choices=["cakephp2", "cakephp3", "cakephp4"],
        default="cakephp2"
    )

    # =========================
    # MERGE
    # =========================
    merge = sub.add_parser("merge")

    merge.add_argument("controller")
    merge.add_argument("model")

    merge.add_argument(
        "--adapter",
        choices=["cakephp2", "cakephp3", "cakephp4"],
        default="cakephp2"
    )

    # =========================
    # PROMPT
    # =========================
    prompt = sub.add_parser("prompt")

    prompt.add_argument("entity")
    prompt.add_argument("controller")
    prompt.add_argument("model")

    prompt.add_argument(
        "--mode",
        choices=["impact", "refactor"],
        default="impact"
    )

    prompt.add_argument(
        "--adapter",
        choices=["cakephp2", "cakephp3", "cakephp4"],
        default="cakephp2"
    )

    # =========================
    # SNAPSHOT
    # =========================
    snapshot = sub.add_parser("snapshot")

    snapshot.add_argument("name")
    snapshot.add_argument("controller")
    snapshot.add_argument("model")

    snapshot.add_argument(
        "--adapter",
        choices=["cakephp2", "cakephp3", "cakephp4"],
        default="cakephp2"
    )

    # =========================
    # MEMORY
    # =========================
    mem = sub.add_parser("memory")

    mem.add_argument("--last", type=int)
    mem.add_argument("--timeline", action="store_true")
    mem.add_argument("--search", type=str)

    mem.add_argument("--snapshots", action="store_true")
    mem.add_argument("--snapshot-show", type=str)

    args = parser.parse_args()

    # =========================
    # ADAPTER ROUTING
    # =========================
    if args.adapter == "cakephp2":

        if args.command == "scan":
            return run_scan(args)

        if args.command == "impact":
            return run_impact(args)

        if args.command == "merge":
            return run_merge(args)

        if args.command == "prompt":
            return run_prompt(args)

        # =========================
        # SNAPSHOT
        # =========================
        if args.command == "snapshot":

            entity_model = build_runtime_entity_model(
                args.controller,
                args.model
            )

            return create_snapshot(
                args.name,
                entity_model
            )

        # =========================
        # MEMORY
        # =========================
        if args.command == "memory":

            if args.snapshots:
                return show_snapshots()

            if args.snapshot_show:
                return show_snapshot(args.snapshot_show)

            if args.timeline:
                return show_timeline()

            if args.search:
                return search(args.search)

            return show_last(args.last or 20)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
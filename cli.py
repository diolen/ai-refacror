import argparse
from analysis.adapters.cakephp2.runner import (
    run_scan,
    run_impact,
    run_merge
)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--adapter",
        choices=["cakephp2", "cakephp3", "cakephp4"],
        default="cakephp2"
    )

    sub = parser.add_subparsers(dest="command")

    scan = sub.add_parser("scan")
    scan.add_argument("file")
    scan.add_argument(
        "--adapter",
        choices=["cakephp2", "cakephp3", "cakephp4"],
        default="cakephp2"
    )

    impact = sub.add_parser("impact")
    impact.add_argument("entity")
    impact.add_argument("controller")
    impact.add_argument("model")
    impact.add_argument(
        "--adapter",
        choices=["cakephp2", "cakephp3", "cakephp4"],
        default="cakephp2"
    )

    merge = sub.add_parser("merge")
    merge.add_argument("controller")
    merge.add_argument("model")
    merge.add_argument(
        "--adapter",
        choices=["cakephp2", "cakephp3", "cakephp4"],
        default="cakephp2"
    )

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

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
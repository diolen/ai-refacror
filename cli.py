import argparse

from analysis.adapters.cakephp2.runner import (
    run_scan,
    run_impact,
    run_merge,
    run_prompt
)


def main():

    parser = argparse.ArgumentParser(
        description="AI Refactor System CLI"
    )

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

    # =========================
    # IMPACT
    # =========================
    impact = sub.add_parser("impact")
    impact.add_argument("entity")
    impact.add_argument("controller")
    impact.add_argument("model")

    # =========================
    # MERGE
    # =========================
    merge = sub.add_parser("merge")
    merge.add_argument("controller")
    merge.add_argument("model")

    # =========================
    # PROMPT
    # =========================
    prompt = sub.add_parser("prompt")
    prompt.add_argument("entity")
    prompt.add_argument("controller")
    prompt.add_argument("model")
    prompt.add_argument("--mode", choices=["impact", "refactor"], default="impact")

    args = parser.parse_args()

    # =========================
    # ADAPTER CHECK
    # =========================
    if args.adapter != "cakephp2":
        print(f"[error] unsupported adapter: {args.adapter}")
        return 1

    # =========================
    # ROUTER
    # =========================
    if args.command == "scan":
        return run_scan(args)

    if args.command == "impact":
        return run_impact(args)

    if args.command == "merge":
        return run_merge(args)

    if args.command == "prompt":
        return run_prompt(args)

    # =========================
    # FALLBACK
    # =========================
    print("[error] no command provided. use --help")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
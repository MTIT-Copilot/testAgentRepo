from __future__ import annotations

import argparse
from agentlab.utils import greet


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="agentlab", description="Agent Lab CLI")
    p.add_argument("name", help="Name to greet")  # TODO: default and validation
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

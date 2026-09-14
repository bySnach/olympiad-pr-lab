"""A tiny command-line demo for the study planner."""

import argparse
from datetime import date
from typing import List, Optional

from .planner import StudyPlanner, StudyTask


def demo_planner() -> StudyPlanner:
    return StudyPlanner(
        [
            StudyTask("A-1", "Algebra warm-up", 30, "high", date(2026, 9, 20)),
            StudyTask("G-1", "Geometry review", 45, "medium", date(2026, 9, 22)),
        ]
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Show a study-plan summary.")
    parser.add_argument(
        "command", choices=["summary", "list"], nargs="?", default="summary"
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    planner = demo_planner()

    if args.command == "list":
        for task in planner.all_tasks():
            print(f"{task.task_id}: {task.title} ({task.minutes} min)")
        return 0

    print(f"Tasks: {len(planner.all_tasks())}")
    print(f"Average minutes: {planner.average_minutes()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

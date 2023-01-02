import argparse

from .objects import InserterClock


def parse_args() -> argparse.Namespace:
    """
    Define an argument parser and return the parsed arguments
    """
    parser = argparse.ArgumentParser(
        prog="ficc",
        description="Generates factorio blueprints for inserter clocks.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--rate",
        "-r",
        type=float,
        required=True,
        help="Count of items to be carried per second (float)",
    )
    parser.add_argument(
        "--stack",
        "-s",
        type=int,
        default=12,
        help="The item or inserter stack size, whichever is lower",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    clock = InserterClock(args.rate, args.stack)

    print(clock)


if __name__ == "__main__":
    main()

# EOF

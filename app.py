"""Estimate tile quantities from floor area, tile dimensions and a waste allowance. All dimensions use centimetres."""

import argparse


def positive(text):
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("Expected an integer of at least 1")
    return value


def nonnegative(text):
    value = int(text)
    if value < 0:
        raise argparse.ArgumentTypeError("Expected an integer of at least 0")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("length", type=positive)
    parser.add_argument("width", type=positive)
    parser.add_argument("tile_length", type=positive)
    parser.add_argument("tile_width", type=positive)
    parser.add_argument("waste", type=nonnegative)
    args = parser.parse_args()
    try:
        required = args.length * args.width * (100 + args.waste)
        coverage = args.tile_length * args.tile_width * 100
        print(f"Tiles to order: {(required + coverage - 1) // coverage}")
    except ValueError as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()

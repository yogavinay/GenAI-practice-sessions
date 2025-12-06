"""Interactive helper to choose or set the default CSV used by plotting scripts.

Usage:
    python set_data.py            # will list CSVs and ask to choose
    python set_data.py --path X   # set default to given path
"""
import argparse
import glob
import os
from csv_config import set_csv_path


def list_csvs():
    return sorted(glob.glob("*.csv"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--path", help="Path to CSV to set as default")
    args = p.parse_args()

    if args.path:
        if not os.path.exists(args.path):
            print(f"File not found: {args.path}")
            return
        set_csv_path(args.path)
        print(f"Default CSV set to: {args.path}")
        return

    csvs = list_csvs()
    if not csvs:
        print("No CSV files found in the current directory.")
        return

    print("Found CSV files:")
    for i, f in enumerate(csvs, start=1):
        print(f"  {i}. {f}")

    try:
        choice = int(input("Choose file number to set as default (0 to cancel): "))
    except Exception:
        print("Invalid choice.")
        return

    if choice <= 0 or choice > len(csvs):
        print("Cancelled or invalid number.")
        return

    selected = csvs[choice - 1]
    set_csv_path(selected)
    print(f"Default CSV set to: {selected}")


if __name__ == "__main__":
    main()

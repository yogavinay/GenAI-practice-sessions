"""Count plot script

Usage: python count_plot.py --csv data.csv --col Species
"""
import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from csv_config import get_csv_path


def plot_count(csv_path: str, column: str):
    df = pd.read_csv(csv_path)
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x=column, palette="Set2")
    plt.title(f"Count Plot: {column}")
    plt.tight_layout()
    plt.show()


def main():
    p = argparse.ArgumentParser(description="Count plot from CSV column")
    p.add_argument("--csv", default=None, help="Path to CSV file (overrides configured default)")
    p.add_argument("--col", default="division", help="Categorical column to plot")
    args = p.parse_args()
    csv_path = args.csv if args.csv else get_csv_path()
    plot_count(csv_path, args.col)


if __name__ == "__main__":
    main()

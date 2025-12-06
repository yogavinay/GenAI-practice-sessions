"""KDE plot script

Usage: python kde_plot.py --csv data.csv --col SepalLengthCm [--hue Species]
"""

import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from csv_config import get_csv_path


def plot_kde(csv_path: str, column: str, hue: str | None = None):
    df = pd.read_csv(csv_path)
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    if hue and hue in df.columns:
        sns.kdeplot(data=df, x=column, hue=hue, fill=True, alpha=0.5)
        plt.title(f"KDE: {column} by {hue}")
    else:
        sns.kdeplot(data=df, x=column, fill=True, alpha=0.5)
        plt.title(f"KDE: {column}")
    plt.tight_layout()
    plt.show()


def main():
    p = argparse.ArgumentParser(description="KDE plot from CSV column")
    p.add_argument("--csv", default=None, help="Path to CSV file (overrides configured default)")
    p.add_argument("--col", default="sales", help="Numeric column to plot")
    p.add_argument("--hue", default="division", help="Optional categorical column for hue")
    args = p.parse_args()
    csv_path = args.csv if args.csv else get_csv_path()
    plot_kde(csv_path, args.col, args.hue)


if __name__ == "__main__":
    main()

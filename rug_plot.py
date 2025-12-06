"""Rug plot script

Usage: python rug_plot.py --csv data.csv --col SepalLengthCm
"""
import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from csv_config import get_csv_path


def plot_rug(csv_path: str, column: str):
    df = pd.read_csv(csv_path)
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 4))
    sns.rugplot(data=df, x=column, height=0.05, color="black", alpha=0.7, linewidth=1)
    plt.title(f"Rug Plot: {column}")
    plt.tight_layout()
    plt.show()


def main():
    p = argparse.ArgumentParser(description="Rug plot from CSV column")
    p.add_argument("--csv", default=None, help="Path to CSV file (overrides configured default)")
    p.add_argument("--col", default="sales", help="Numeric column to plot")
    args = p.parse_args()
    csv_path = args.csv if args.csv else get_csv_path()
    plot_rug(csv_path, args.col)

    


if __name__ == "__main__":
    main()

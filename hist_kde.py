"""Histogram + KDE plot script

Usage: python hist_kde.py --csv C:\Users\vinay\OneDrive\Desktop\genai\dm_office_sales.csv --col SepalLengthCm
"""
import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from csv_config import get_csv_path


def plot_hist_kde(csv_path: str, column: str, bins: int = 20):
    df = pd.read_csv(csv_path)
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x=column, bins=bins, kde=True, color='blue', alpha=0.6)
    plt.title(f"Histogram + KDE: {column}")
    plt.tight_layout()
    plt.show()


def main():
    p = argparse.ArgumentParser(description="Histogram + KDE from CSV column")
    p.add_argument("--csv", default=None, help="Path to CSV file (overrides configured default)")
    p.add_argument("--col", default="sales", help="Numeric column to plot")
    p.add_argument("--bins", type=int, default=20, help="Number of histogram bins")
    args = p.parse_args()
    csv_path = args.csv if args.csv else get_csv_path()
    plot_hist_kde(csv_path, args.col, args.bins)


if __name__ == "__main__":
    main()

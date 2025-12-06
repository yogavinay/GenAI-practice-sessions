"""Create three plots side-by-side: Rug, Histogram+KDE, Count.

Usage examples:
  python three_plots.py
  python three_plots.py --csv dm_office_sales.csv --col sales --cat division --out three.png
"""
import argparse
from typing import Optional

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from csv_config import get_csv_path


def three_plots(csv_path: str, col: str = "sales", cat: str = "division", out: Optional[str] = None):
    df = pd.read_csv(csv_path)
    sns.set(style="whitegrid")

    fig, axes = plt.subplots(1, 3, figsize=(18, 10))

    # 1) Rug plot (left)
    sns.rugplot(data=df, x=col, height=0.05, color="black", alpha=0.7, linewidth=1, ax=axes[0])
    axes[0].set_title(f"Rug Plot: {col}")

    # 2) Histogram + KDE (middle)
    sns.histplot(data=df, x=col, bins=30, kde=True, color='tab:blue', alpha=0.6, ax=axes[1])
    axes[1].set_title(f"Histogram + KDE: {col}")

    # 3) Count plot (right)
    if cat in df.columns:
        sns.countplot(data=df, x=cat, palette="Set2", order=df[cat].value_counts().index, ax=axes[2])
        axes[2].set_title(f"Count Plot: {cat}")
        axes[2].tick_params(axis='x', rotation=45)
    else:
        axes[2].text(0.5, 0.5, f"Column '{cat}' not found", ha='center', va='center')
        axes[2].set_title("Count Plot")

    plt.tight_layout()

    if out:
        fig.savefig(out, dpi=150, bbox_inches='tight')
        print(f"Saved figure to: {out}")
    else:
        plt.show()


def main():
    p = argparse.ArgumentParser(description="Three side-by-side plots (rug, hist+kde, count)")
    p.add_argument("--csv", default=None, help="CSV path (overrides configured default)")
    p.add_argument("--col", default="sales", help="Numeric column for rug/hist/kde")
    p.add_argument("--cat", default="division", help="Categorical column for count plot")
    p.add_argument("--out", default=None, help="Optional output image path (PNG) to save instead of showing")
    args = p.parse_args()

    csv_path = args.csv if args.csv else get_csv_path()
    three_plots(csv_path, args.col, args.cat, args.out)


if __name__ == "__main__":
    main()

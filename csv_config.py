import os

CONFIG_FILE = "data_csv.txt"


def get_csv_path(default: str = "data.csv") -> str:
    """Return the configured CSV path if set, otherwise return `default`."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                path = f.read().strip()
            if path:
                return path
        except Exception:
            pass
    return default


def set_csv_path(path: str) -> None:
    """Write the CSV path to the config file."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(path)

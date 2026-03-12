from datetime import datetime

from src.common.finance import download_asset


def main():
    print("Hello from proyecto-guiado!")

    # example: get Apple daily data for January 2020
    try:
        df = download_asset("AAPL", "2020-01-01", "2020-01-31")
        print(df.head())
    except Exception as exc:
        print("download failed:", exc)


if __name__ == "__main__":
    main()

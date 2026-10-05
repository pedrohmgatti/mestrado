import pandas as pd


def main():
    df = pd.read_csv("data/car_evaluation.csv")
    print(df.head())
    print(df.info())


if __name__ == "__main__":
    main()

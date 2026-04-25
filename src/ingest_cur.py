import pandas as pd

def load_cur_data(file_path):
    df = pd.read_csv(file_path)
    print("\n✅ CUR data loaded successfully\n")
    print(df)
    return df

if __name__ == "__main__":
    df = load_cur_data("data/sample_cur_data.csv")

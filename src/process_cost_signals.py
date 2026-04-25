import pandas as pd

def classify_cost_signal(row):
    if row["service"] == "EC2" and row["usage_quantity"] >= 200:
        return "⚠️ Growth-driven usage - partially commit"

    elif row["service"] == "EC2" and row["usage_quantity"] < 120:
        return "✅ Stable baseline - safe to commit"

    elif row["service"] == "Lambda" and row["usage_quantity"] > 100000:
        return "❌ Possible inefficiency - investigate before committing"

    else:
        return "Review"

def process_cost_signals(file_path):
    df = pd.read_csv(file_path)
    df["finops_signal"] = df.apply(classify_cost_signal, axis=1)

    print("\n✅ Cost signals processed successfully\n")
    print(df)

    df.to_csv("data/processed_output.csv", index=False)
    print("\n✅ Output saved to data/processed_output.csv")

if __name__ == "__main__":
    process_cost_signals("data/sample_cur_data.csv")

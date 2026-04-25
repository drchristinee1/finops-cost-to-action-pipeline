import pandas as pd
import json

def generate_jira_payloads(file_path):
    df = pd.read_csv(file_path)

    action_items = df[df["finops_signal"] != "Review"]

    payloads = []

    for _, row in action_items.iterrows():
        payload = {
            "summary": f"FinOps Action Required: {row['service']} cost signal",
            "description": (
                f"Account ID: {row['account_id']}\n"
                f"Service: {row['service']}\n"
                f"Usage Type: {row['usage_type']}\n"
                f"Cost: ${row['cost']}\n"
                f"Usage Quantity: {row['usage_quantity']}\n"
                f"FinOps Signal: {row['finops_signal']}\n\n"
                "Recommended Action: Review usage pattern and assign engineering owner."
            ),
            "labels": ["finops", "cost-action", row["service"].lower()]
        }

        payloads.append(payload)

    print("\n✅ Jira payloads generated successfully\n")
    print(json.dumps(payloads, indent=2))

    with open("data/jira_payloads.json", "w") as f:
        json.dump(payloads, f, indent=2)

    print("\n✅ Output saved to data/jira_payloads.json")

if __name__ == "__main__":
    generate_jira_payloads("data/processed_output.csv")

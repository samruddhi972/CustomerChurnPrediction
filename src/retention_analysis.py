import json
import pandas as pd

from predict import predict_churn
from retention_strategy import recommend_retention_action


DATA_FILE = "data/E Commerce Dataset.xlsx"
OUTPUT_FILE = "predictions/customer_retention_recommendations.csv"


def run_retention_analysis():
    # Load the actual customer dataset
    df = pd.read_excel(DATA_FILE, sheet_name="E Comm")

    results = []

    print(f"Loaded {len(df)} customer records.")
    print("Generating churn predictions and retention recommendations...")

    for _, customer in df.iterrows():
        customer_data = customer.to_frame().T

        # Predict churn using the trained model
        prediction = predict_churn(customer_data)

        # Use actual customer behaviour for retention recommendations
        customer_details = customer.to_dict()

        recommendation = recommend_retention_action(
            customer_details,
            prediction["risk_category"]
        )

        results.append({
            "CustomerID": customer.get("CustomerID"),
            "ChurnProbability": round(
                prediction["churn_probability"], 4
            ),
            "PredictedChurn": prediction["predicted_churn"],
            "RiskCategory": recommendation["risk_category"],
            "RetentionPriority": recommendation["priority"],
            "RecommendedActions": " | ".join(
                recommendation["recommended_actions"]
            )
        })

    # Save the final customer-level results
    output = pd.DataFrame(results)

    output.to_csv(OUTPUT_FILE, index=False)

    print("\nRetention Analysis Completed Successfully!")
    print(f"Customers analysed: {len(output)}")
    print(f"Output saved to: {OUTPUT_FILE}")

    print("\nRisk category distribution:")
    print(output["RiskCategory"].value_counts())

    print("\nSample recommendations:")
    print(output.head(5).to_string(index=False))


if __name__ == "__main__":
    run_retention_analysis()
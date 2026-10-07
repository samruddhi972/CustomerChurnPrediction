Customer Churn Prediction System

A machine learning-based Customer Churn Prediction System that identifies customers who are likely to leave an e-commerce platform. The system generates a churn probability, assigns a customer to a Low, Medium, or High risk category, and can be integrated with a Streamlit dashboard for interactive prediction and retention analysis.

---

📌 Project Overview

Customer churn is a major challenge for e-commerce businesses. Identifying customers who are likely to churn allows businesses to take preventive action and improve customer retention.

This project uses machine learning to:

- Analyze customer behavior and characteristics
- Predict the probability of customer churn
- Classify customers into risk categories
- Identify important factors associated with churn
- Provide predictions that can support customer retention strategies
- Integrate the trained model into a Streamlit application

---

🎯 Objectives

1. Understand and preprocess customer data.
2. Analyze the factors associated with customer churn.
3. Train and compare multiple machine learning models.
4. Select and tune the best-performing model.
5. Optimize the classification threshold for churn prediction.
6. Generate churn probabilities for individual customers.
7. Categorize customers into Low, Medium, and High risk.
8. Provide the trained model for Streamlit integration.
9. Support targeted customer retention strategies.

---

📊 Dataset

The project uses an E-Commerce Customer Churn dataset containing:

- 5,630 customers
- 20 columns
- Customer behavioral, demographic, transactional, and service-related information.

Important Features

Some of the features used by the model include:

- Tenure
- Preferred Login Device
- City Tier
- Warehouse to Home
- Preferred Payment Mode
- Gender
- Hour Spend on App
- Number of Devices Registered
- Preferred Order Category
- Satisfaction Score
- Marital Status
- Number of Addresses
- Complaints
- Order Amount Hike from Last Year
- Coupon Used
- Order Count
- Days Since Last Order
- Cashback Amount

The "CustomerID" column is treated as an identifier rather than a predictive feature.

---

🔄 Machine Learning Pipeline

The ML workflow consists of the following stages:

Dataset
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Missing Value Handling
   ↓
Feature Preparation
   ↓
Train / Validation / Test Split
   ↓
Baseline Model Comparison
   ↓
Model Selection
   ↓
Hyperparameter Tuning
   ↓
Threshold Optimization
   ↓
Final Evaluation
   ↓
Churn Probability
   ↓
Risk Classification
   ↓
Saved Model

---

🧹 Data Preprocessing

The preprocessing pipeline handles both numerical and categorical features.

Numerical Features

- Missing values are handled using median imputation
- Features are standardized where required

Categorical Features

- Missing values are handled using most-frequent imputation
- Categorical variables are converted using One-Hot Encoding
- Unknown categories are safely handled during prediction

The preprocessing steps are included within the machine learning pipeline to ensure consistent processing during both training and prediction.

---

🤖 Models Evaluated

The project compares multiple machine learning models, including:

- Logistic Regression
- Random Forest
- Extra Trees

The best-performing candidate was selected based on Precision-Recall AUC (PR-AUC).

Final Model

Extra Trees Classifier

The model was further tuned using hyperparameter optimization, followed by classification-threshold optimization.

---

📈 Model Performance

The final tuned model achieved the following results on the unseen test set:

Metric| Score
Accuracy| 97.34%
Precision| 91.67%
Recall| 92.63%
F1-Score| 0.9215
ROC-AUC| 0.9963

The optimized classification threshold was:

0.4553

This threshold was selected using the validation set to provide a better balance between precision and recall.

---

🔍 Key Churn Drivers

The feature importance analysis identified the following major contributors:

Feature| Importance
Tenure| 24.99%
Cashback Amount| 9.31%
Complain| 6.54%
Warehouse to Home| 6.01%

Interpretation

Tenure was the strongest feature in the model, indicating that the length of a customer's relationship with the platform is strongly associated with churn risk.

Other important factors include cashback behavior, complaints, and the distance between the warehouse and the customer's home.

These findings can be used to support targeted customer retention strategies.

---

⚠️ Customer Risk Classification

The model generates a churn probability for each customer.

Customers are categorized into three risk levels:

Low Risk       → Probability < 0.40
Medium Risk    → 0.40 – < 0.70
High Risk      → Probability ≥ 0.70

Example:

Customer
   ↓
Churn Probability = 0.82
   ↓
High Risk

The risk classification can be used by the retention component of the project to determine appropriate interventions.

---

💾 Generated Artifacts

The ML pipeline produces the following important files:

"customer_churn_model.joblib"

Contains:

- Trained machine learning model
- Optimized classification threshold
- Feature metadata
- Risk classification rules

This file is used for prediction and can be integrated directly into the Streamlit application.

"customer_churn_predictions.csv"

Contains batch predictions for the test customers, including:

- Churn probability
- Predicted churn class
- Risk category

---

🖥️ Streamlit Integration

The trained model is designed to be integrated with a Streamlit frontend.

The intended workflow is:

User enters customer information
            ↓
       Streamlit App
            ↓
 customer_churn_model.joblib
            ↓
    ML Prediction
            ↓
 Churn Probability
            ↓
 Low / Medium / High Risk
            ↓
 Retention Recommendation

A prediction interface can be exposed through:

result = predict_churn(customer_data)

Example output:

{
    "churn_probability": 0.82,
    "predicted_class": 1,
    "risk_level": "High"
}

---

📁 Project Structure

Customer-Churn-Prediction/
│
├── data/
│   └── E Commerce Dataset.xlsx
│
├── notebooks/
│   ├── churn_analysis.ipynb
│   └── CCP.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── model/
│   └── customer_churn_model.joblib
│
├── predictions/
│   └── customer_churn_predictions.csv
│
├── app/
│   └── streamlit_app.py
│
├── requirements.txt
│
└── README.md

---

⚙️ Installation

Clone the repository:

git clone <repository-url>
cd Customer-Churn-Prediction

Install the required Python packages:

pip install -r requirements.txt

---

▶️ Running the ML Pipeline

Place the dataset in the appropriate "data/" directory and run the training pipeline.

The pipeline will

1. Load the dataset
2. Preprocess the data
3. Train baseline models
4. Select the best candidate
5. Tune the model
6. Optimize the classification threshold
7. Evaluate the final model
8. Generate predictions
9. Save the trained model

---

🚀 Running the Streamlit Application

After the trained model has been generated:

streamlit run app/streamlit_app.py

The application can then be used to enter customer information and obtain an individual churn prediction.

---

👥 Team Contributions

This project is developed as a four-person team.

Person 1 — Machine Learning Model

- Dataset analysis
- Data preprocessing
- Exploratory analysis
- Model training
- Model comparison
- Hyperparameter tuning
- Threshold optimization
- Model evaluation
- Feature importance analysis
- Churn probability generation
- Model serialization

Person 2 — Frontend / Streamlit

- Streamlit dashboard
- Customer input interface
- Prediction display
- Risk visualization
- Integration with the trained ML model

Person 3 — Retention Strategy & Risk Analysis

- Customer risk interpretation
- Retention strategies
- High-risk customer analysis
- Mapping risk categories to recommended actions

Person 4 — Integration, Testing & Documentation

- System integration
- Testing
- Error handling
- Documentation
- Final project coordination

---

🔮 Future Improvements

Possible future improvements include:

- Testing additional machine learning algorithms
- Advanced hyperparameter optimization
- Explainable AI techniques such as SHAP
- Automated retention recommendations
- Real-time prediction monitoring
- Model retraining using new customer data
- Deployment as a web application
- Monitoring model performance after deployment

---

🧰 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- OpenPyXL
- Streamlit
- Jupyter / Google Colab

---

📌 Conclusion

The Customer Churn Prediction System uses machine learning to identify customers who are at risk of leaving an e-commerce platform.

The final Extra Trees model achieved strong performance on the unseen test set, with 91.67% precision, 92.63% recall, 92.15% F1-score, and 99.63% ROC-AUC.

The resulting churn probabilities and risk categories can be integrated into a Streamlit application and combined with targeted retention strategies to help businesses proactively engage high-risk customers.

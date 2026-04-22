#💳 Fraud Detection System using Machine Learning

## 📌 Overview

This project focuses on detecting fraudulent financial transactions using machine learning. Fraud detection is a critical problem in the financial sector, where identifying suspicious activities early can prevent significant losses.

The system analyzes transaction-level data and predicts whether a transaction is **fraudulent** or **legitimate** based on learned patterns.
## 📂 Project Structure

```
├── fraud_detection.py
├── fraud_detection_model.pkl
├── Fraud_Detection_.ipynb
├── AIML Dataset.csv
└── README.md
```

## 📊 Dataset

The dataset (AIML Dataset.csv) contains financial transaction records used to train and evaluate the model.

🔑 Key Features

* **step** – Represents a unit of time (transaction sequence)
* **type** – Type of transaction (PAYMENT, TRANSFER, CASH_OUT, etc.)
* **amount** – Transaction amount
* **oldbalanceOrg** – Sender’s balance before transaction
* **newbalanceOrig** – Sender’s balance after transaction
* **oldbalanceDest** – Receiver’s balance before transaction
* **newbalanceDest** – Receiver’s balance after transaction
* **isFraud** – Target variable (0 = Legitimate, 1 = Fraud)

## 🚀 Installation

### 1️⃣ Clone the repository:

```bash
https://github.com/abhinandan07-git/Fraud-detection-Model.git
```

### 2️⃣ Install dependencies:



Install them with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
Run the Project


```bash
python fraud_detection.py
```
## 🔍 Methodology

The project follows a structured machine learning workflow:

1. **Data Preprocessing**

* Handling missing values
* Encoding categorical variables
* Feature selection

2. **Exploratory Data Analysis (EDA)**

* Understanding data distribution
* Detecting class imbalance
* Visualizing key patterns

3. **Model Training**

* Splitting dataset into training and testing sets
* Training machine learning model
* Saving the trained model using pickle

4. **Model Evaluation**

* Evaluating performance using:
    * Accuracy
    * Precision
    * Recall
    * F1-score

5. **Prediction**

* Using the trained model (fraud_detection_model.pkl) to classify new transactions
## 📊 Visualizations

Some visualizations generated during the analysis include:

![alt text](https://github.com/27abhishek27/British-Airways-Job-Simulation/blob/main/British_Airways_Task1_png/histogram.png)
![alt text](https://github.com/27abhishek27/British-Airways-Job-Simulation/blob/main/British_Airways_Task1_png/Rating.png)
![alt text](https://github.com/27abhishek27/British-Airways-Job-Simulation/blob/main/British_Airways_Task1_png/full%20reviewpng.png)
![alt text](https://github.com/27abhishek27/British-Airways-Job-Simulation/blob/main/British_Airways_Task1_png/recommended.png)

*(Presentations contain detailed visuals.)*

## 🛠️ Technologies Used

* **Python**
* **Pandas & NumPy** – Data manipulation
* **Matplotlib & Seaborn** – Data visualization
* **Scikit-learn** – Machine learning model building
* **Pickle** – Model serialization

## 📌 Future Improvements

📌 Future Improvements

* Implement advanced models (XGBoost, LightGBM)
* Handle class imbalance using SMOTE
* Perform hyperparameter tuning
* Deploy as a web application (Flask/Streamlit)
* Add real-time fraud detection capabilities

⸻

##📌 Conclusion

This project demonstrates how machine learning can be effectively applied to detect fraudulent financial transactions. With proper feature engineering and model tuning, the system can significantly improve fraud detection accuracy.
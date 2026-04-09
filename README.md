# 💳 Credit Card Fraud Detection System

## 📌 Overview

This project is a **Machine Learning-based Credit Card Fraud Detection System** that predicts whether a transaction is **fraudulent or legitimate**.

The model is trained on a real-world dataset and deployed using an interactive **Streamlit web application** for easy testing and demonstration.

---

## 🚀 Features

* Detects fraudulent transactions in real-time
* User-friendly web interface using Streamlit
* Handles imbalanced dataset using SMOTE
* Pre-trained ML model for quick predictions
* Sample input buttons for easy demo

---

## 🧠 Tech Stack

* **Programming Language:** Python
* **Libraries:** NumPy, Pandas, Scikit-learn, Imbalanced-learn
* **Frontend/UI:** Streamlit
* **Model Storage:** Pickle (.pkl)

---

## ⚙️ Machine Learning Algorithm

* **Random Forest Classifier**
* Used for classification of transactions into:

  * Legitimate (0)
  * Fraudulent (1)

---

## 📊 Dataset

* Source: Kaggle Credit Card Fraud Dataset
* Contains anonymized features (V1 to V28) and transaction amount
* Highly imbalanced dataset (fraud cases are very rare)

---

## 🖥️ How It Works

1. User enters transaction details (29 features)
2. Input is processed and converted into numerical format
3. Pre-trained model predicts the result
4. Output is displayed as:

   * ✅ Legitimate Transaction
   * 🚨 Fraudulent Transaction

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rishika180/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

---

## 📷 Demo

The application provides:

* Input field for transaction data
* Sample data buttons for quick testing
* Real-time prediction results

---

## 📈 Future Improvements

* Add transaction history tracking
* Improve UI/UX design
* Deploy on cloud (Streamlit Cloud / AWS)
* Use deep learning models for better accuracy

---

## 👩‍💻 Author

**Rishika Agrawal**

---

## ⭐ Conclusion

This project demonstrates how machine learning can be applied to **detect financial fraud efficiently** and help in building secure digital payment systems.










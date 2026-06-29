Success
**Overview**

The UPI Fraud Detection System is a machine learning-based 
web application that detects whether a UPI transaction is fraudulent or legitimate.
The system allows users to upload transaction data in CSV format, processes each
transaction using a trained machine learning model, and displays the prediction
results through an easy-to-use web interface.
This project is designed to assist banks, payment service providers, and financial institutions in identifying potentially fraudulent transactions before they are completed.

## Features

- Detects fraudulent and legitimate UPI transactions.
- Uploads transaction data using CSV files.
- Predicts fraud for multiple transactions at once.
- Displays prediction results in a user-friendly interface.
- Allows users to download prediction results as a CSV file.
- Fast and lightweight Flask web application.
- Machine Learning-based prediction model for fraud detection.
This is a professional, well-formatted `README.md` section that you can directly copy and paste into GitHub.

# 🛠️ Technologies Used

| Category                 | Technologies                    |
| ------------------------ | ------------------------------- |
| **Programming Language** | Python                          |
| **Machine Learning**     | Scikit-learn, Pandas, NumPy     |
| **Web Development**      | Flask, HTML, CSS                |
| **Development Tools**    | Visual Studio Code, Git, GitHub |

---

# 📁 Project Structure

```text
UPI_Fraud_Detection/
│
├── app.py
├── fraud_model.pkl
├── model/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── uploads/
├── outputs/
├── test.csv
├── test_transaction.csv
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The machine learning model is trained using a UPI transaction dataset containing the following features:

* Transaction Amount
* Merchant Category
* Transaction Time
* Device Type
* Location
* Transaction Frequency
* Previous Transaction History
* Transaction Label (Fraud / Legitimate)

---

# 🤖 Machine Learning Model

The project uses a **supervised machine learning classification algorithm** to detect fraudulent UPI transactions.

### Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Serialization using Pickle (`.pkl`)
7. Deployment using Flask

---

# 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AishwaryaC-2004/UPI_Fraud-detection.git
```

### 2. Navigate to the Project Folder

```bash
cd UPI_Fraud-detection
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install the Required Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask Application

```bash
python app.py
```

### 7. Open in Your Browser

```text
http://127.0.0.1:5000
```

---

# 💻 How to Use

1. Start the Flask application.
2. Open the application in your web browser.
3. Upload a CSV file containing UPI transaction data.
4. Click the **Predict** button.
5. View the prediction results.
6. Download the prediction report as a CSV file.

---

# 📈 Output

The application classifies each transaction into one of the following categories:

* ✅ Legitimate Transaction
* 🚨 Fraudulent Transaction

The generated output CSV includes:

* Original transaction details
* Predicted class (Fraud / Legitimate)


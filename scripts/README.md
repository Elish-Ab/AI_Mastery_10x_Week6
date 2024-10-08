
---

# Scripts Directory

This folder contains the Python script used to deploy the trained credit scoring model as a REST API. The API allows for real-time predictions of credit scores based on transaction data.

## Overview of `app.py`

- **app.py**:  
  This script serves the trained Random Forest model via a Flask-based API. It includes an endpoint `/predict` that accepts transaction data and returns the predicted credit risk score for a customer.

### How to Run the API

1. Ensure you have installed all the required packages:
   ```bash
   pip install -r ../requirements.txt

2. Navigate to the scripts/ directory:
   ```bash
   cd scripts
3. Run the app.py script:
   ```bash
   python app.py
4. The API will be available at http://localhost:5000/predict.

# API Usage

  ```markdown
    Endpoint: /predict

    Method: POST

    Payload: Send a JSON object containing the transaction data. Example payload:
```
  ```bash
    {
      "TransactionId": "123456",
      "AccountId": "78910",
      "CustomerId": "55555",
      "ProductCategory": "Electronics",
      "Amount": 500.0,
      "TransactionStartTime": "2024-10-01T12:34:56"
    }
```



Let me know if you'd like to make any changes or add more details!

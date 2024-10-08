from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
log_reg_model = joblib.load('log_reg_model.pkl')



@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the JSON data from the request
    try:
        # Extract features and ensure the input matches the expected shape
        features = np.array([[data['TransactionId'],
                              data['BatchId'],
                              data['AccountId'],
                              data['SubscriptionId'],
                              data['CustomerId'],
                              data['ProviderId'],
                              data['ProductId'],
                              data['ChannelId'],
                              data['Amount'],
                              data['PricingStrategy'],
                              data['year'],
                              data['month'],
                              data['day'],
                              data['hour'],
                              data['ProductCategory_encoded'],
                              data['FraudResult_y'],
                              data['CustomerId_woe'],
                              data['BatchId_woe'],
                              data['ProductCategory_encoded_woe'],
                              data['PricingStrategy_woe'],
                              data['hour_woe'],
                              data['SubscriptionId_woe'],
                              data['TransactionId_woe'],
                              data['ChannelId_woe'],
                              data['day_woe'],
                              data['Amount_woe'],
                              data['AccountId_woe'],
                              data['ProductId_woe'],
                              data['month_woe'],
                              data['ProviderId_woe'],
                              data['year_woe']]])

        prediction = log_reg_model.predict(features)  # Make prediction

        # Convert prediction to standard Python types
        return jsonify({'prediction': int(prediction[0])})  # Convert to int if prediction is an integer
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return error if any issue occurs

if __name__ == '__main__':
    app.run(debug=True)

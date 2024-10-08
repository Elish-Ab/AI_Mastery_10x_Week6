# Credit Scoring Model for Buy-Now-Pay-Later (BNPL) Service

This repository contains the code and notebooks for building a credit scoring model for a Buy-Now-Pay-Later (BNPL) service. The project is divided into five tasks, each covering a different stage of the credit risk prediction pipeline. 

## Project Structure

The repository is structured as follows:

- `notebooks/`: Contains Jupyter notebooks for tasks 1 through 4. These tasks involve data exploration, feature engineering, model building, and model tuning.
- `scripts/`: Contains the code for task 5, where the model is deployed as a REST API.
- `requirements.txt`: List of dependencies needed to run the project.
- `README.md`: This file, explaining the structure and purpose of the repository.

## Tasks Overview

1. **Task 1: Data Collection and Exploration**  
   - Data cleaning and exploratory data analysis (EDA) to understand the data and extract insights.
   
2. **Task 2: Feature Engineering**  
   - Creation of new features and data transformations required for model building.

3. **Task 3: Model Building and Evaluation**  
   - Training multiple machine learning models to predict credit risk and evaluating their performance.

4. **Task 4: Model Tuning and Selection**  
   - Hyperparameter tuning and final model selection based on evaluation metrics like accuracy, precision, recall, F1 score, and ROC-AUC.

5. **Task 5: Model Deployment**  
   - Building a REST API using Flask to serve the trained model for real-time predictions.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Elish-Ab/AI_Mastery_10x_Week6.git
   cd AI_Mastery_10x_Week6
2. Install all libarries and packages
   ```bash
   pip install -r requirements.txt
   
## To run the API for real-time credit scoring predictions:

1. Navigate to the scripts/ directory:
  ```bash
    cd scripts
    python app.py



# Healthcare Premium Prediction

This project predicts health insurance costs based on user attributes such as age, medical history, smoking status, BMI category, and employment details. The system is built using **Streamlit** for the web interface and **machine learning models** trained on different age groups to make predictions.

## Features
- Interactive **Streamlit** web application.
- Predicts health insurance premium based on user inputs.
- Uses **XGBoost** models trained for different age groups.
- **Scikit-learn** for preprocessing and scaling data.
- Models and scalers are preloaded using **joblib**.

## Live Demo
You can access the deployed app here:
[Healthcare Premium Prediction - Streamlit](https://mlhealthcare-premium-prediction.streamlit.app/)

## File Structure
```
├── main.py                         # Streamlit web app for user input and prediction
├── prediction_helper.py             # Helper functions for preprocessing and prediction
├── requirements.txt                 # Dependencies required to run the project
├── artifacts/                       # Folder containing trained models and scalers
│   ├── model_young.joblib
│   ├── model_rest.joblib
│   ├── scaler_young.joblib
│   ├── scaler_rest.joblib
├── Notebooks/                       # Jupyter Notebooks for model training and analysis
│   ├── data_segmentation.ipynb
│   ├── ml_premium_prediction.ipynb
│   ├── ml_premium_prediction_rest.ipynb
│   ├── ml_premium_prediction_rest_with_gr.ipynb
│   ├── ml_premium_prediction_young.ipynb
│   ├── ml_premium_prediction_young_with_gr.ipynb
```

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/healthcare-premium-prediction.git
    cd healthcare-premium-prediction
    ```
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate  # For Windows
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application Locally
To start the **Streamlit** web application locally, run:
```bash
streamlit run main.py
```

## How it Works
1. Users provide input values such as age, medical history, BMI, smoking status, etc.
2. The **Streamlit UI** captures the inputs and passes them to `prediction_helper.py`.
3. Data is **preprocessed and scaled** using appropriate models.
4. The prediction model is selected based on the user's age:
   - If **Age ≤ 25** → Uses `model_young.joblib`
   - If **Age > 25** → Uses `model_rest.joblib`
5. The predicted insurance premium is displayed.

## Technologies Used
- **Python** (3.9+ recommended)
- **Streamlit** (Web interface)
- **Scikit-learn** (Preprocessing)
- **XGBoost** (Model Training)
- **Pandas** & **NumPy** (Data Handling)
- **Joblib** (Model Persistence)

## Contributing
Feel free to fork this repository and submit pull requests.

Credits: Codebasics

---



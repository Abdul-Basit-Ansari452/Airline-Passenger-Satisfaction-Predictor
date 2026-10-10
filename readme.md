Airline Passenger Satisfaction
Predicting airline passenger satisfaction using machine learning.

Project Overview
Binary classification: satisfied vs not satisfied
Dataset: 129,880 airline passenger survey records
Models compared: Logistic Regression, KNN, SVM, Random Forest
Best model: Random Forest (~96% accuracy)
How to Run
Open the notebook in notebooks/ to see the full analysis and training
For the Streamlit app:
cd app
pip install streamlit scikit-learn pandas joblib
streamlit run app.py
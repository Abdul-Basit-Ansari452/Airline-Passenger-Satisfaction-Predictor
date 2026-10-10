import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Airline Passenger Satisfaction")

st.title("Airline Passenger Satisfaction Predictor")
st.caption("Predicts whether a passenger will be satisfied based on flight and service details.")

model = joblib.load("rf_model (1).pkl")

st.sidebar.header("Passenger Details")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
customer_type = st.sidebar.selectbox("Customer Type", ["Loyal Customer", "disloyal Customer"])
age = st.sidebar.slider("Age", 7, 85, 40)
travel_type = st.sidebar.selectbox("Type of Travel", ["Business travel", "Personal Travel"])
flight_class = st.sidebar.selectbox("Class", ["Business", "Eco", "Eco Plus"])
flight_distance = st.sidebar.number_input("Flight Distance", 31, 5000, 1000)
departure_delay = st.sidebar.number_input("Departure Delay (minutes)", 0, 1600, 0)
arrival_delay = st.sidebar.number_input("Arrival Delay (minutes)", 0, 1600, 0)

st.header("Service Ratings")

rating_options = [0, 1, 2, 3, 4, 5]

col1, col2, col3 = st.columns(3)

with col1:
    wifi = st.selectbox("Inflight wifi service", rating_options, index=3)
    time_convenient = st.selectbox("Departure/Arrival time convenient", rating_options, index=3)
    online_booking = st.selectbox("Ease of Online booking", rating_options, index=3)
    gate_location = st.selectbox("Gate location", rating_options, index=3)

with col2:
    food_drink = st.selectbox("Food and drink", rating_options, index=3)
    online_boarding = st.selectbox("Online boarding", rating_options, index=3)
    seat_comfort = st.selectbox("Seat comfort", rating_options, index=3)
    entertainment = st.selectbox("Inflight entertainment", rating_options, index=3)

with col3:
    onboard_service = st.selectbox("On-board service", rating_options, index=3)
    leg_room = st.selectbox("Leg room service", rating_options, index=3)
    baggage = st.selectbox("Baggage handling", rating_options, index=3)
    checkin = st.selectbox("Checkin service", rating_options, index=3)

cleanliness = st.selectbox("Cleanliness", rating_options, index=3)

if st.button("Predict"):
    input_data = pd.DataFrame({
        "Gender": [1 if gender == "Female" else 0],
        "Customer Type": [1 if customer_type == "Loyal Customer" else 0],
        "Age": [age],
        "Type of Travel": [1 if travel_type == "Business travel" else 0],
        "Flight Distance": [flight_distance],
        "Inflight wifi service": [wifi],
        "Departure/Arrival time convenient": [time_convenient],
        "Ease of Online booking": [online_booking],
        "Gate location": [gate_location],
        "Food and drink": [food_drink],
        "Online boarding": [online_boarding],
        "Seat comfort": [seat_comfort],
        "Inflight entertainment": [entertainment],
        "On-board service": [onboard_service],
        "Leg room service": [leg_room],
        "Baggage handling": [baggage],
        "Checkin service": [checkin],
        "Cleanliness": [cleanliness],
        "Departure Delay in Minutes": [departure_delay],
        "Arrival Delay in Minutes": [arrival_delay],
        "Class_Business": [1 if flight_class == "Business" else 0],
        "Class_Eco": [1 if flight_class == "Eco" else 0],
        "Class_Eco Plus": [1 if flight_class == "Eco Plus" else 0],
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    if prediction:
        st.success(f"Prediction: Satisfied (confidence {probability[1]:.1%})")
    else:
        st.error(f"Prediction: Not Satisfied (confidence {probability[0]:.1%})")
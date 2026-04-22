# Fraud Detection App using Streamlit


#importing the libraries for  building the streamlit web app
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model=joblib.load('fraud_detection_model.pkl')

# Set up the Streamlit app
st.title("Fraud Detection App")
st.markdown("please  Enter the details to predict if the transaction is fraudulent or not")
st.divider()



# User input for transaction details
transaction_type=st.selectbox("Transaction Type", ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
amount=st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrig=st.number_input("Old Balance Origin(sender)", min_value=0.0, value=10000.0)
newbalanceOrig=st.number_input("New Balance Origin(sender)", min_value=0.0, value=9000.0)
oldbalanceDest=st.number_input("Old Balance Destination(receiver)", min_value=0.0, value=0.0)
newbalanceDest=st.number_input("New Balance Destination(receiver)", min_value=0.0, value=0.0)

# Prepare the input data for prediction
if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrig], 
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest],
        'balanceDiff': [amount],
        'balanceDiffDest': [oldbalanceDest - newbalanceDest],
        'balanceDiffOrig': [oldbalanceOrig - newbalanceOrig]        
    })
    
    # Make the prediction using the loaded model
    prediction = model.predict(input_data)[0]
    st.subheader(f"Prediction Result: {prediction}")
    
    # Display the result to the user
    if prediction == 1:
        st.error("The transaction is predicted to be fraudulent.")
    else:
        st.success("The transaction is predicted to be legitimate.")
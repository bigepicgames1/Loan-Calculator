import streamlit as st
import pandas as pd
import math

# Title and Input Fields
st.title("Loan Repayment Calculator")
st.write("### Input Data")
col1, col2 = st.columns(2)

home_value = col1.number_input("Loan Amount (₹)", min_value=0, value=100000, step=10000)
deposit = col1.number_input("Down Payment (₹)", min_value=0, value=10000, step=10000)
interest_rate = col2.number_input("Annual Interest Rate (in %)", min_value=0.0, value=7.5, step=0.1)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, max_value=50, value=5)
prepayment = st.number_input("Annual Prepayment Amount (₹)", min_value=0, value=10000, step=10000)

# Calculate loan parameters
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

# Initialize repayment and amortization variables
total_payments = 0
total_interest = 0
remaining_balance = loan_amount
schedule = []
prepayment_applied_years = 0

# Amortization with prepayment applied annually
for i in range(1, number_of_payments + 1):
    # Calculate monthly interest and principal payments
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    
    # Apply prepayment at the end of each year
    if prepayment > 0 and i % 12 == 0:
        remaining_balance -= prepayment
        prepayment_applied_years += 1
    
    # Deduct monthly principal from remaining balance
    remaining_balance -= principal_payment

    # Track cumulative payments and interest
    total_payments += monthly_payment
    total_interest += interest_payment

    # Break loop if balance is paid off
    if remaining_balance <= 0:
        remaining_balance = 0
        schedule.append([i, monthly_payment, principal_payment, interest_payment, remaining_balance, math.ceil(i / 12)])
        break

    # Append each month’s details to the schedule
    schedule.append([i, monthly_payment, principal_payment, interest_payment, remaining_balance, math.ceil(i / 12)])

# Convert schedule to DataFrame for display
df = pd.DataFrame(
    schedule,
    columns=["Month", "EMI Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

# Display repayment summary
st.write("### Repayment Summary with Prepayment")
col1, col2, col3 = st.columns(3)
col1.metric(label="Monthly EMI", value=f"₹{monthly_payment:,.2f}")
col2.metric(label="Total Payment", value=f"₹{total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"₹{total_interest:,.0f}")

# Display the adjusted amortization schedule as a chart and table
st.write("### Annual Remaining Balance After Prepayments")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df)

with st.expander("View Full Amortization Schedule with Prepayments"):
    st.dataframe(df, width=670)

# Calculate interest savings
original_total_interest = (monthly_payment * number_of_payments) - loan_amount
interest_savings = original_total_interest - total_interest

st.write("### Prepayment Benefit Summary")
st.metric(label="Interest Savings", value=f"₹{interest_savings:,.0f}")
st.metric(label="Loan Ends in    (years)", value=f"{prepayment_applied_years + remaining_balance / loan_amount * loan_term:.1f}")

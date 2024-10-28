# Loan Repayment Calculator

This is a **Loan Repayment Calculator** application built using Streamlit. It calculates monthly loan payments, total interest, and demonstrates the impact of prepayments on the overall loan repayment schedule. Hosted [here](https://loan-calculator-bigepicgames1.streamlit.app/).

## Features

- **Input fields** to enter loan amount, down payment, interest rate, loan term, and annual prepayment amount.
- **Monthly EMI calculation** based on the loan amount, interest rate, and loan term.
- **Prepayment calculation** to show how annual prepayments impact the loan balance.
- **Repayment Summary** including:
  - Monthly EMI amount
  - Total payment and interest
  - Interest savings with prepayments
  - Remaining loan term after prepayments
- **Amortization Schedule Table** that displays details of principal, interest, and remaining balance for each month.
- **Interactive Chart** showing the annual remaining balance over the loan term.

## Getting Started

To run this project locally:

### Prerequisites
- Install Python 3.x
- Install Streamlit and Pandas:
  ```bash
  pip install streamlit pandas
Running the App
Clone this repository.
Navigate to the project folder.
Start the Streamlit app:
bash
Copy code
streamlit run app.py
Open your browser to http://localhost:8501.
Usage
Enter Loan Details: Fill in the loan amount, down payment, interest rate, loan term, and annual prepayment.
Review Summary: View monthly EMI, total payment, and potential interest savings.
Analyze Schedule: Check the amortization schedule table and the remaining balance over the years.
Sample Code
The main calculation logic uses a loop to apply monthly and annual prepayments, calculating the EMI based on:

python
Copy code
monthly_payment = (
    loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)
Deployment
This app is deployed on Streamlit Cloud at Loan Repayment Calculator.

License
This project is licensed under the MIT License. See the LICENSE file for details.

import matplotlib.pyplot as plt
import numpy as np
from loan_calculator import Apartment, Loan, CustomerDividend, MonthlyCost
from config import EQUITY


osterhaus_gate_8b = Apartment(
    price=6.69e6, joint_expenses=3929
)
loan = Loan(
    amount=osterhaus_gate_8b.price - EQUITY,
    nominal_rate=0.0492,
    years=30
)
dividend = CustomerDividend(
    deposit=0,
    borrowers=2
)
expenses = MonthlyCost(
    loan=loan,
    apartment=osterhaus_gate_8b,
    customer_dividend=dividend
)
print(expenses.get_monthly_cost())

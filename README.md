# Loan Calculator

A loan calculator that estimates monthly expenses for each month over a loan payment schedule.

## Features

### General


* Calculates monthly interest rate from nominal rate and length of payment schedule.
* Calculates loan amount based on:

  * Total purchase price of the property
  * Total equity and number borrowers
* Toggleable metrics:

  * Customer dividend
  * Tax deduction
  * Interest-rate stress testing*
* Calculates the eligible loan amount based on income and equity*.

### Annuity

Calculates the projected monthly payment of a loan based on:

* Monthly interest rate
* Loan amount
* Length of the payment schedule

### Customer Dividend

Calculates projected customer dividend for each month over the payment schedule based on:

* Outstanding loan balance , including the initial balance at month zero
* Number of borrowers
* Loan and loan limit per borrower
* Deposit and deposit limit per borrower during the previous calendar year
* Dividend rate

### Tax Deduction

Calculates the projected tax deduction for each month over a payment schedule based on:

* Projected interest payment
* Tax deduction rate

### Monthly Expenses

Calculates the projected monthly expenses for each month over the payment schedule based on:

* Projected outstanding loan balance
* Projected interest payment
* Projected customer dividend
* Projected tax deduction
* Monthly joint property expenses

## Configuration

* See **config.py** to adjust settings.

## Known Issues

* Customer dividend is a conservative estimate.
* *Not implemented yet.

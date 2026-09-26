# Smart Electricity Bill Calculator

A beginner-friendly Python console program that asks for customer details and electricity usage, then prints a formatted bill.

## Run the program

```bash
python smart_electricity_bill.py
```

## Billing rates

Energy is charged progressively, so each rate applies only to the units in its range:

| Units | Rate per unit |
| --- | ---: |
| First 100 | Rs. 2 |
| 101 to 200 | Rs. 4 |
| 201 to 500 | Rs. 6 |
| Above 500 | Rs. 8 |

A fixed service charge of Rs. 100 is added to the energy charge. The request lists both 5,000 and 500 as the upper slab boundary; this program follows the stated “above 500” cutoff.

## Program flow

1. `get_customer_details()` asks for the customer's name and ID, then reads the consumed units. It repeats the units prompt if the input is not a number or is negative.
2. `calculate_bill(units)` calculates the energy charge across the progressive rate ranges, adds the fixed service charge, and returns the energy charge, service charge, and final amount.
3. `display_bill(...)` prints the customer details, units consumed, energy charge, service charge, and final amount in a formatted bill.
4. `main()` calls the three functions in order and starts when the program is run directly.

The program uses only Python's built-in features. It does not use a database, files for bill storage, APIs, external libraries, or classes.
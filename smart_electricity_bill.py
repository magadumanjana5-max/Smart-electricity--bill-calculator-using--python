SERVICE_CHARGE = 100


def get_customer_details():
    """Ask for customer information and return it with validated units."""
    customer_name = input("Enter customer name: ")
    customer_id = input("Enter customer ID: ")

    while True:
        try:
            units = float(input("Enter electricity units consumed: "))
            if units < 0:
                print("Units consumed cannot be negative. Please try again.")
            else:
                return customer_name, customer_id, units
        except ValueError:
            print("Please enter a valid number of units.")


def calculate_bill(units):
    """Calculate progressive energy charges and return the bill amounts."""
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = 100 * 2 + (units - 100) * 4
    elif units <= 500:
        energy_charge = 100 * 2 + 100 * 4 + (units - 200) * 6
    else:
        energy_charge = 100 * 2 + 100 * 4 + 300 * 6 + (units - 500) * 8

    final_amount = energy_charge + SERVICE_CHARGE
    return energy_charge, SERVICE_CHARGE, final_amount


def display_bill(customer_name, customer_id, units, energy_charge,
                 service_charge, final_amount):
    """Print a formatted electricity bill."""
    print("\n" + "=" * 40)
    print("           ELECTRICITY BILL")
    print("=" * 40)
    print(f"Customer name:   {customer_name}")
    print(f"Customer ID:     {customer_id}")
    print(f"Units consumed:  {units:.2f}")
    print("-" * 40)
    print(f"Energy charge:   Rs. {energy_charge:.2f}")
    print(f"Service charge:  Rs. {service_charge:.2f}")
    print("-" * 40)
    print(f"Final amount:    Rs. {final_amount:.2f}")
    print("=" * 40)


def main():
    customer_name, customer_id, units = get_customer_details()
    energy_charge, service_charge, final_amount = calculate_bill(units)
    display_bill(customer_name, customer_id, units, energy_charge,
                 service_charge, final_amount)


if __name__ == "__main__":
    main()

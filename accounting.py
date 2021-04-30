melon_cost = 1.00

def customer_payment(path):
    """Opens file, tokenizes llines, prints statement if expected amount not equal to paid amount """
    customer_orders = open(path) # Open file at path
    # Iterate over lines in file
    for line in customer_orders:
        # Strip whitespace from end of line
        line = line.rstrip()
        # Split line along '|' to get list of strings
        words = line.split('|')
        # Unpack list of strings and name variables
        cust_num, cust_name, cust_melons, cust_paid = words
    cust_melons = int(cust_melons) # Change variable type from 'str' to 'int'
    cust_paid = float(cust_paid) # Change variable type from 'str' to 'float'

    # Calculate expected cost of customer order
    cust_expect = (cust_melons*melon_cost)
    
    # Compare expected cost to what customer paid, if different, print statement with customer name, what was expected, and what they paid
    if cust_expect != cust_paid:
        print(f"{cust_name} paid ${cust_paid:.2f},",
            f"expected ${cust_expect:.2f}")
    # Close the file
    customer_orders.close()
    #return

# Call the function
customer_payment("/home/hackbright/src/homework/accounting/customer-orders.txt")

#*** Hackbright starting code below***
customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
          f"expected ${customer1_expected:.2f}"
          )

customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print(f"{customer2_name} paid ${customer2_paid:.2f},",
          f"expected ${customer2_expected:.2f}"
          )

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print(f"{customer3_name} paid ${customer3_paid:.2f},",
          f"expected ${customer3_expected:.2f}"
          )

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print(f"{customer4_name} paid ${customer4_paid:.2f},",
          f"expected ${customer4_expected:.2f}"
          )

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print(f"{customer5_name} paid ${customer5_paid:.2f},",
          f"expected ${customer5_expected:.2f}"
          )

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print(f"{customer6_name} paid ${customer6_paid:.2f},",
          f"expected ${customer6_expected:.2f}"
          )

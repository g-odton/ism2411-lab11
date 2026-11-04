# customers.py
# Author: Grace Odton
# Module 11 Lab: Dictionaries

# exercise 1: one customer
customer = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'tier': 'gold',
    'ytd_spend': 12400
}

print(customer['name'])
print(customer['email'])
print(customer['tier'])
print(customer['ytd_spend'])
print(customer)
print()

# exercise 2: update and add
customer['phone'] = '813-555-0142'
print(customer)
customer['tier'] = 'platinum'
del customer['email']
print(customer)
print(customer.get('email', 'Email not found'))

# exercise 3: safe lookup


# exercise 4: iterate


# exercise 5: look up table


# exercise 6: list of dicts


# exercise 7: nested catalog


# exercise 8: sales by region

# self assessment (((((((( 2-3 sentences )))))
# 1. in real work, get() would be used
# 2. this pattern reminds me of ____ in excel
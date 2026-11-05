# customers.py
# Author: Grace Odton
# Module 11 Lab: Dictionaries

# exercise 1: one customer
print('exercise 1: one customer')
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
print('exercise 2: update and add')
customer['phone'] = '813-555-0142'
print(customer)
customer['tier'] = 'platinum'
del customer['email']
print(customer)

# exercise 3: safe lookup
print('exercise 3: safe lookup')

# new
print(customer.get('email', 'Email not found'))

# old
# try: 
#     print(customer['email'])
# except KeyError as error:
#     print(f'KeyError caught: {error}')
print()

# exercise 4: iterate
print('exercise 4: iterate')
for key, value in customer.items():
    print(f'{key} : {value}')

for item in customer:
    print(item)
print()

# exercise 5: look up table
print('exercise 5: look up table')
tier_discounts = {'bronze': 0,
                  'silver': 0.05,
                  'gold': 0.10,
                  'platinum': 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer['tier'], 0)
final_price = purchase * (1 - discount_rate)

print(f'Tier: {customer['tier']}')
print(f'Discount: {discount_rate * 100:.0f}')
print(f'Final Price: ${final_price:.2f}')
print()

# exercise 6: list of dicts
print('exercise 6: list of dicts')
customers = [
    {'name': 'Bob', 'tier': 'silver', 'ytd_spend': 3200},
    {'name': 'Carol', 'tier': 'gold', 'ytd_spend': 8750},
    {'name': 'David', 'tier': 'bronze', 'ytd_spend': 450}
]
for record in customers:
    rate = tier_discounts.get(record['tier'], 0)
    discount = 300 * rate # assuming a purchase of 300 for each customer
    print(f'{record['name']}, {record['tier']}: ${discount:.2f} discount on $300 purchase.')
print()

# exercise 7: nested catalog
print('exercise 7: nested catalog')
catalog = {
    "Widget A": {'price': 9.99, 'stock': 150},
    'Gadget C': {'price': 49.99, 'stock': 8}
}
for product, details in catalog.items():
    if details['stock'] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")
print()

# exercise 8: sales by region
print('exercise 8: sales by region')
transactions = [
    {'region': 'South', 'amount': 300},
    {'region': 'North', 'amount': 150},
    {'region': 'South', 'amount': 200},]
sales_by_region = {}
for sale in transactions:
    region = sale['region']
    sales_by_region[region] = sales_by_region.get(region, 0) + sale['amount']
print(sales_by_region) # prints raw dictionary with sales totals by region

for region in sorted(sales_by_region): # prints pretty output with sales totals by region
    print(f'{region}: {sales_by_region[region]}')

# self assessment (((((((( 2-3 sentences )))))
# 1. in real work, get() could be used when there's a missing part of the information file at work and you want to avoid it, while bracket notation could be used when the information is under a specific name and all parts are filled in. The rule of thumb would probably be whether an error would occur when selecting the variable.
# 2. this pattern reminds me of a pivot table in excel. the python version may be more useful because excel is full of bloatware and thus probably can't run as many simulations as regular python code can.
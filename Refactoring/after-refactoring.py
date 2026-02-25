# After Refactoring (Guard Clauses)
def ship(order):
    print("Product sended")

def send_confirmation(email):
    print(f"Send code to {email}.")

def process_order(order):
    if order is None:
        raise Exception("No order")
    if not order.is_paid:
        raise Exception("Not paid")
    if not order.has_items:
        raise Exception("No items")
    if order.customer is None:
        raise Exception("No customer")
    if not order.customer.is_active:
        raise Exception("Inactive customer")

    # Happy Path
    ship(order)
    send_confirmation(order.customer.email)

class MockOrder:
    def __init__(self, is_paid, has_items, customer):
        self.is_paid = is_paid
        self.has_items = has_items
        self.customer = customer

class MockCustomer:
    def __init__(self, is_active, email):
        self.is_active = is_active
        self.email = email

def run_tests():
    try:
        process_order(None)
    except Exception as e:
        print(f"Test 1 passed. Error: {e}")

    customer = MockCustomer(is_active=True, email="muhammadazizxabibullayev@gmail.com")
    order = MockOrder(is_paid=True, has_items=True, customer=customer)
    print("Test 2 is starting...")
    process_order(order)
    print("Test 2 passed.")

run_tests()

# After refactoring, I use Guard Clauses.
# I check for errors at the start and stop the function if something is wrong.
# This makes the 'Happy Path' (the normal result) very clear and easy to find.

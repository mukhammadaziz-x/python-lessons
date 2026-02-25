# Before Refactoring
def process_order(order):
    if order is not None:
        if order.is_paid:
            if order.has_items:
                if order.customer is not None:
                    if order.customer.is_active:
                        ship(order)
                        send_confirmation(order.customer.email)
                    else:
                        raise Exception("Inactive customer")
                else:
                    raise Exception("No customer")
            else:
                raise Exception("No items")
        else:
            raise Exception("Not paid")
    else:
        raise Exception("No order")

# In the first example, the code is difficult to follow because it has many if statements inside each other.
# If the user is missing or inactive, the error is handled at the very end.
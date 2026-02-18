# Before Refactoring
# def get_discount(user, price):
#     if user is not None:
#         if user.is_active:
#             if price > 100:
#                 return price * 0.1
#             else:
#                 return 0
#         else:
#             raise Exception("User inactive")
#     else:
#         raise Exception("No user")

# In the first example, the code is difficult to follow because it has many if statements inside each other.
# If the user is missing or inactive, the error is handled at the very end.

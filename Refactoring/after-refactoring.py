# After Refactoring (Guard Clauses)
# def get_discount(user, price):
#     if user is None:
#         raise Exception("No user")
#     if not user.is_active:
#         raise Exception("User inactive")
#
#     # (Happy path) open and understandable
#     return price * 0.1 if price > 100 else 0

# After refactoring, I use Guard Clauses.
# I check for errors at the start and stop the function if something is wrong.
# This makes the 'Happy Path' (the normal result) very clear and easy to find.

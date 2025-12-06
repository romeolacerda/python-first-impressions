def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:2.f} is due: {due_date}")

display_invoice("JoeSchmo", 42.50, "01/01")
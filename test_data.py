login_data = [
    ("invalid@email.com", "wrongpassword"),
    ("test@email.com", "wrongpassword"),
    ("user123@email.com", "wrongpassword"),
    ("", "wrongpassword"),        # blank email
    ("invalid@email.com", ""),    # blank password
    ("", "")                      # both blank
]
from kiteconnect import KiteConnect

api_key = "12bvngsg45ecld9a"
api_secret = "rwz5xr3dlm460jrcbx1ne4orj6jfhomm"

kite = KiteConnect(api_key=api_key)

# Generate login URL to be visited by the user
print("Login URL:", kite.login_url())

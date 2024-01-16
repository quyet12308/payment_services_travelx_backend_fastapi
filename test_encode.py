from urllib.parse import quote_plus

url = "http://sandbox.vnpayment.vn/return_payment"

encoded_url = quote_plus(url)

print(encoded_url)
import qrcode
import json
data = {
  "recipient_name": "John Doe",

  "account_number": "1234567890", 
  "bank_name": "Vietcombank",
  "amount": 100000,
  "description": "Payment for order #123"
}

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(json.dumps(data))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("invoice_qrcode.png")
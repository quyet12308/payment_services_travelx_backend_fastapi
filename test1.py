import requests
from setting import *

# Tạo header với api key
headers = {
    "Authorization": f"Bearer {vapi_vnappmob_infor['api_key']}"
}

# Gửi yêu cầu GET đến API
response = requests.get(f"{vapi_vnappmob_infor['url']}", headers=headers)

# Kiểm tra trạng thái trả về của API
if response.status_code == 200:
    # Nếu thành công, trả về dữ liệu JSON
    data = response.json()
    print(data)
else:
    # Nếu không thành công, in ra lỗi
    print("Lỗi khi lấy dữ liệu từ API:", response.status_code)
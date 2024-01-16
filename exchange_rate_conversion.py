from setting import *
import requests
def get_exchange_rate():
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
        # print(data)
        return data["results"]
    else:
        # Nếu không thành công, in ra lỗi
        print("Lỗi khi lấy dữ liệu từ API:", response.status_code)

def exchange_rate_conversion(data_list,num_usd):
    for data in data_list:
        if data["currency"] == "USD":
            rate = data["sell"]
            num_vnd = num_usd * rate
            return num_vnd
        
    
# list_rate = get_exchange_rate()
# b = exchange_rate_conversion(data_list=list_rate,num_usd=100)
# print(b)
# print(type(b))
# print(int(b))
# a = get_exchange_rate()
# print(a)
# print(type(a))
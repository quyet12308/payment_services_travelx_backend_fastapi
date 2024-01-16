import hashlib
import urllib.parse
from urllib.parse import quote_plus
import datetime
import pytz

def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y%m%d%H%M%S")
    return t

def gettime3():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%H%M%S")
    return t

def build_vnpay_url(vnp_amount, vnp_command, vnp_create_date, vnp_curr_code, vnp_ip_addr, 
                   vnp_locale, vnp_order_info, vnp_order_type, vnp_return_url, 
                   vnp_tmn_code, vnp_txn_ref, vnp_version):
  
    url = "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html?"

    params = {
        "vnp_Amount": vnp_amount,
        "vnp_Command": vnp_command, 
        "vnp_CreateDate": vnp_create_date,
        "vnp_CurrCode": vnp_curr_code,
        "vnp_IpAddr": vnp_ip_addr,
        "vnp_Locale": vnp_locale,
        "vnp_OrderInfo": vnp_order_info, 
        "vnp_OrderType": vnp_order_type,
        "vnp_ReturnUrl": vnp_return_url,
        "vnp_TmnCode": vnp_tmn_code,
        "vnp_TxnRef": vnp_txn_ref,
        "vnp_Version": vnp_version
    }

    query_string = urllib.parse.urlencode(params)
    params["vnp_SecureHash"] = hashlib.sha256((query_string + "MUkYCq2fbtlX0I6oW3xG").encode()).hexdigest()

    return url + query_string

import hashlib

def build_vnpay_url2(vnp_Amount, vnp_Command, vnp_CreateDate, vnp_CurrCode, vnp_IpAddr, vnp_Locale, vnp_OrderInfo, vnp_OrderType, vnp_ReturnUrl, vnp_TmnCode, vnp_TxnRef, vnp_Version, vnp_HashSecret):
    base_url = "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html"
    params = {
        "vnp_Amount": vnp_Amount,
        "vnp_Command": vnp_Command,
        "vnp_CreateDate": vnp_CreateDate,
        "vnp_CurrCode": vnp_CurrCode,
        "vnp_IpAddr": vnp_IpAddr,
        "vnp_Locale": vnp_Locale,
        "vnp_OrderInfo": vnp_OrderInfo,
        "vnp_OrderType": vnp_OrderType,
        "vnp_ReturnUrl": vnp_ReturnUrl,
        "vnp_TmnCode": vnp_TmnCode,
        "vnp_TxnRef": vnp_TxnRef,
        "vnp_Version": vnp_Version
    }
    # Sort the parameters by key in ascending order
    sorted_params = sorted(params.items(), key=lambda x: x[0])
    # Build the query string
    query_string = "&".join([f"{key}={value}" for key, value in sorted_params])
    # Append the hash secret to the query string
    # query_string += f"&vnp_HashSecret={vnp_HashSecret}"
    # Calculate the SHA256 hash of the query string
    # secure_hash = hashlib.sha256(query_string.encode('UTF-8')).hexdigest()
    secure_hash = hashlib.sha256(string=query_string.encode('UTF-8'),usedforsecurity=vnp_HashSecret).hexdigest()
    # Append the secure hash to the query string
    query_string += f"&vnp_SecureHash={secure_hash}"
    # Combine the base URL and the query string
    url = f"{base_url}?{query_string}"
    return url



# Example usage
url = build_vnpay_url2(
    vnp_Amount=100000,
    vnp_Command="pay",
    # vnp_CreateDate="20240115122911",
    vnp_CreateDate=gettime2(),
    vnp_CurrCode="VND",
    # vnp_IpAddr="127.0.0.1",
    vnp_IpAddr="42.119.159.154",
    vnp_Locale="VN",
    # vnp_OrderInfo="nap+tien+test+lan+1",
    vnp_OrderInfo=urllib.parse.quote_plus("nap tien test lan1"),
    vnp_OrderType="other",
    vnp_ReturnUrl=quote_plus("http://localhost:8014/return_payment"),
    # vnp_ReturnUrl="http://localhost:8014/return_payment",
    # vnp_ReturnUrl="http://sandbox.vnpayment.vn/return_payment",
    vnp_TmnCode="1T1ZDPPG",
    vnp_TxnRef="2030",
    # vnp_TxnRef=gettime3(),
    vnp_Version="2.1.0",
    vnp_HashSecret="EKFCVOAIWKHETSKIDMWSRBZLSDYPWOKC"
)
print(url)


# print(gettime2())
# print(type(gettime2()))

# a = build_vnpay_url(
#     vnp_amount="100000",
#     vnp_command="pay",
#     vnp_create_date="20240114103111",
#     vnp_curr_code="vnd",
#     vnp_ip_addr="127.0.0.1",
#     vnp_locale="vn",
#     vnp_order_info="nap tien test lan 1",
#     vnp_order_type="other",
#     vnp_return_url="http://localhost:8014/return_payment",
#     vnp_tmn_code="1T1ZDPPG",
#     vnp_txn_ref="1914",
#     vnp_version="2.1.0",

# )
# print(a)


"https://sandbox.vnpayment.vn/paymentv2/vpcpay.html?vnp_Amount=1806000&vnp_Command=pay&vnp_CreateDate=20210801153333&vnp_CurrCode=VND&vnp_IpAddr=127.0.0.1&vnp_Locale=vn&vnp_OrderInfo=Thanh+toan+don+hang+%3A5&vnp_OrderType=other&vnp_ReturnUrl=https%3A%2F%2Fdomainmerchant.vn%2FReturnUrl&vnp_TmnCode=DEMOV210&vnp_TxnRef=5&vnp_Version=2.1.0&vnp_SecureHash=3e0d61a0c0534b2e36680b3f7277743e8784cc4e1d68fa7d276e79c23be7d6318d338b477910a27992f5057bb1582bd44bd82ae8009ffaf6d141219218625c42"
"http://sandbox.vnpayment.vn/paymentv2/vpcpay.html?vnp_Amount=10000000&vnp_BankCode=NCB&vnp_Command=pay&vnp_CreateDate=20170829103111&vnp_CurrCode=VND&vnp_IpAddr=172.16.68.68&vnp_Locale=vn&vnp_Merchant=DEMO&vnp_OrderInfo=Nap+tien+cho+thue+bao+0123456789.+So+tien+100%2c000&vnp_OrderType=topup&vnp_ReturnUrl=http%3a%2f%2fsandbox.vnpayment.vn%2ftryitnow%2fHome%2fVnPayReturn&vnp_TmnCode=2QXUI4J4&vnp_TxnRef=23554&vnp_Version=2&vnp_SecureHashType=SHA256&vnp_SecureHash=e6ce09ae6695ad034f8b6e6aadf2726f"
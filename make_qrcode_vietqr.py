
from setting import payment_qr_infor
from unidecode import unidecode


def unidecode_str(str):
    chuoi_khong_dau = unidecode(str).replace(" ", "%20")
    return chuoi_khong_dau
base_url_img_qr = "https://img.vietqr.io/image/vietinbank-113366668888-compact2.jpg?amount=790000&addInfo=dong%20qop%20quy%20vac%20xin&accountName=Quy%20Vac%20Xin%20Covid"

base_url_img_qr_1 = "https://img.vietqr.io/image/bidv-4505054853-compact2.jpg?amount=790000&addInfo=dong%20qop%20quy%20vac%20xin&accountName=Quy%20Vac%20Xin%20Covid"


def make_url_qr_code_payment_img(AMOUNT,DESCRIPTION,ACCOUNT_NAME):
    base_url = payment_qr_infor["api_base_url"]
    bank_name = payment_qr_infor["bank_name"],
    stk = payment_qr_infor["stk"],
    template = payment_qr_infor["template2"]





import hashlib

def decrypt_sha256(message, secret_key):
    # Kết hợp chuỗi tin nhắn và khóa bí mật
    combined = message + secret_key

    # Tạo đối tượng băm SHA256
    sha256 = hashlib.sha256()

    # Cập nhật đối tượng băm với chuỗi kết hợp
    sha256.update(combined.encode('utf-8'))

    # Lấy giá trị băm cuối cùng dưới dạng chuỗi hex
    hashed_message = sha256.hexdigest()

    return hashed_message

a = decrypt_sha256(
    message="36deb200ef0ee44a4c3a6a1c574aaff5a186da3d9e10d9ef5f9da69779442e15",
    secret_key="EKFCVOAIWKHETSKIDMWSRBZLSDYPWOKC"
)

print(a)
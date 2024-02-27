import hashlib
import base64


def generate_custom_hash(input_string):
    # Получаем MD5
    md5_hash = hashlib.md5(input_string.encode()).digest()

    # Конвертируем хеш в Base64
    base64_encoded = base64.b64encode(md5_hash).decode()

    # Обрезаем результат до 12 символов
    truncated = base64_encoded[:12]

    print(truncated)
    return truncated

custom_hash = generate_custom_hash("Israel-Gaza war")

print(custom_hash)

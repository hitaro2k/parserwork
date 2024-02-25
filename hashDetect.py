import hashlib
import base64


def generate_custom_hash(input_string):
    # Получаем MD5 хеш от входной строки
    md5_hash = hashlib.md5(input_string.encode()).digest()

    # Конвертируем хеш в Base64
    base64_encoded = base64.b64encode(md5_hash).decode()

    # Обрезаем результат до 12 символов
    truncated = base64_encoded[:12]

    return truncated


# Применяем функцию к строке "Israel-Gaza war"
custom_hash = generate_custom_hash("Israel-Gaza war")

print(custom_hash)

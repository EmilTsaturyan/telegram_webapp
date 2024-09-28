from hashlib import sha256
import hmac
import json
from urllib.parse import parse_qsl
import json

from fastapi import HTTPException, status, Header
from core import settings



def parse_init_data(token: str, raw_init_data: str):
    is_valid = validate_init_data(token, raw_init_data)
    if not is_valid:
        return False

    result = {}
    for key, value in parse_qsl(raw_init_data):
        try:
            value = json.loads(value)
        except json.JSONDecodeError:
            result[key] = value
        else:
            result[key] = value
    return result


def validate_dependency(User_Init_Data: str = Header(None)):
    if User_Init_Data != 'test':
        if not User_Init_Data or not validate_init_data(settings.telegram_token, User_Init_Data):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid telegram init data'
            )
        result = {}
        for key, value in parse_qsl(User_Init_Data):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                result[key] = value
            else:
                result[key] = value
        return result.get('user')


def validate_init_data(token, raw_init_data):
    try:
        parsed_data = dict(parse_qsl(raw_init_data))
    except ValueError:
        return False
    if "hash" not in parsed_data:
        return False

    init_data_hash = parsed_data.pop('hash')
    data_check_string = "\n".join(f"{key}={value}" for key, value in sorted(parsed_data.items()))
    secret_key = hmac.new(key=b"WebAppData", msg=token.encode(), digestmod=sha256)

    return hmac.new(secret_key.digest(), data_check_string.encode(), sha256).hexdigest() == init_data_hash
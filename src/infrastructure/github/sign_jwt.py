import time
import jwt


def get_signed_jwt_token(pem_path: str, client_id: str) -> str:
    with open(pem_path, 'rb') as pem_file:
        signing_key = pem_file.read()
    payload = {
        'iat': int(time.time()),
        'exp': int(time.time()) + 600,
        'iss': client_id
    }
    encoded_jwt = jwt.encode(payload, signing_key, algorithm='RS256')
    return encoded_jwt

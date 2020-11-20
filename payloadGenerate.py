import json
import time
import base64


def payloadGenerate(ACCESS_TOKEN):

    # Nonce is positive integer like unix timestamp. To prevent replay attack, user needs to provide the nonce which is increased for each request.
    param = {
        "access_token": ACCESS_TOKEN,
        "price": 500000,
        "qty": 1.1234,
        "nonce": int(time.time() * 1000),
    }

    # to json
    json_param = json.dumps(param)  # Turns your json dict into a str

    # X-COINONE-PAYLOAD
    # Encode JSON string by base64 that is X-COINONE-PAYLOAD.
    # In Python 3.x you need to convert your str object to a bytes object for base64 to be able to encode them.
    payload = base64.b64encode(
        json_param.encode("utf-8")
    )  # encode default: utf-8 하지만 explicit하게 써주자

    return payload

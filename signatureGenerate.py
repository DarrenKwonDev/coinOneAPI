import hashlib
import hmac


def signatureGenerate(SECRET_KEY, payload):
    # X-COINONE-SIGNATURE
    # HMAC(key, msg, digestmod)  key: bytes msg: ReadableBuffer

    # SECRET KEY must be upper case.
    processedSecretKey = SECRET_KEY.upper().encode("utf-8")

    #
    signature = hmac.new(processedSecretKey, payload, hashlib.sha512).hexdigest()

    return signature

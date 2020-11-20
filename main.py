import os
from dotenv import load_dotenv
from payloadGenerate import payloadGenerate
from signatureGenerate import signatureGenerate
import requests
import json

load_dotenv(verbose=True)

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
SECRET_KEY = os.getenv("SECRET_KEY")
APIURL = "https://api.coinone.co.kr"

# X-COINONE-PAYLOAD
payload = payloadGenerate(ACCESS_TOKEN)  # byte 형식임

# X-COINONE-SIGNATURE
signature = signatureGenerate(SECRET_KEY, payload)

# 어차피 송금, 전송 등은 BTC/KRW만 지원하므로 currency를 다른 값으로 두는 것은 의미가 없습니다
ETHERIUM = "ETH"
BITCOIN = "BTC"

# general (전부 get)
ORDERBOOK_URL = f"{APIURL}/orderbook/?currency={BITCOIN}"  # bid/ask 확인 가능
TICKER_URL = f"{APIURL}/ticker/?currency={BITCOIN}"  # ticker
RECENT_COMPLETE_ORDER_URL = f"{APIURL}/trades/?currency={BITCOIN}"  # 최근 체결

# account (전부 post)
BALANCE_URL = f"{APIURL}/v2/account/balance/"
DEPOSIT_URL = f"{APIURL}/v2/account/deposit_address/"
USER_INFO_URL = f"{APIURL}/v2/account/user_info/"
VIRTUAL_ACCOUNT = f"{APIURL}/v2/account/virtual_account/"

# order (전부 post)
CANCEL_ORDER = f"{APIURL}/v2/order/cancel/"
LIMIT_BUY = f"{APIURL}/v2/order/limit_buy/"
LIMIT_SELL = f"{APIURL}/v2/order/limit_sell/"
LIMIT_ORDER = f"{APIURL}/v2/order/limit_orders/"
COMPLETE_ORDER = f"{APIURL}/v2/order/complete_orders"
ORDER_INFORMATION = f"{APIURL}/v2/order/order_info"


def Request(action, URL):
    if action == "GET":

        response = requests.get(
            URL,
            data=payload,
            headers={
                "Content-type": "application/json",
                "X-COINONE-PAYLOAD": payload,
                "X-COINONE-SIGNATURE": signature,
            },
        )

        # beautify
        return json.dumps(response.json(), sort_keys=True, indent=2)

    elif action == "POST":

        response = requests.post(
            URL,
            data=payload,
            headers={
                "Content-type": "application/json",
                "X-COINONE-PAYLOAD": payload,
                "X-COINONE-SIGNATURE": signature,
            },
        )

        return json.dumps(response.json(), sort_keys=True, indent=2)


print(Request("GET", ORDERBOOK_URL))

import requests
import json
import os
import alpaca_trade_api as tradeapi
from config import *

# Setting up environmental variables
os.environ['APCA_API_KEY_ID'] = '[use your own key id here]'
os.environ['APCA_API_SECRET_KEY'] = '[use your own key here]'
os.environ['APCA_API_BASE_URL'] = 'https://paper-api.alpaca.markets'

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
api = tradeapi.REST(api_version='v2')


def main():
    response = create_order("VIX", 3, "buy", "limit", "gtc", 36.00)
    print(response)
    # orders = get_orders()
    # print(orders)

    account = api.get_account()
    aapl = api.alpha_vantage.historic_quotes('AAPL', adjusted=True, output_format='csv', cadence='weekly')
    # print(aapl)



def create_order(symbol, qty, side, type, time_in_force, limit_price=None, stop_price=None, client_order_id=None,
                 order_class=None, take_profit=None, stop_loss=None):
    # data = {
    #     "symbol": symbol,
    #     "qty": qty,
    #     "side": side,
    #     "type": type,
    #     "time_in_force": time_in_force
    # }
    # api.submit_order(json=data)
    return api.submit_order(symbol=symbol,
                            qty=qty,
                            side=side,
                            time_in_force=time_in_force,
                            type=type,
                            client_order_id=client_order_id,
                            stop_price=stop_price,
                            order_class=order_class,
                            limit_price=limit_price,
                            take_profit=dict(
                                limit_price=limit_price,
                            ),
                            stop_loss=dict(
                                stop_price=stop_price,
                                limit_price=limit_price,
                            )
                            )
    # r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    #
    # return json.loads(r.content)


def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)

    return json.loads(r.content)


if __name__ == '__main__':
    main()

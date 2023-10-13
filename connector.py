import requests
import os

def slack_notify(order_id: int, username: str, amount: float):
    details = f'[Details](https://admin.mysite.com/core/order/{order_id})'
    message = f'*{username}* has placed a new order of amount *{amount}*. {details}'
    payload = {'text': message}

    response = requests.post(os.environ.get(
        'WEB_HOOK_SLACK_URL'), data=str(payload))
    return response

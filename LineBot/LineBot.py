from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('U5WM+ylZE6pvqLPcDtKqF4MY7NdjganrZ6Xh/bXqK4vtPgOT/tbUxbi5ec63Pa4HBDEGV3IVMeUKlirxkGlVYaLAryYd6DcZ7sio2t+LJ2SO+OXtMgAEbukW6d6YYjbgdBpjrfg6Em1yaccGBbPjMQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ac91545fac6cab8278e25e55f746d500')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

menu = {
    "漢堡蛋":45,
    "總匯三明治":60
}

shoppingCard = {}

def similar(target, order, threshold=0.6):
    target_set = set(target)
    order_set = set(order)

    intersect = target_set & order_set
    return (len(intersect) / len(target_set)) >= threshold


def compareItem(itemName):
    itemFound = False
    if not similar("多少錢", itemName):
        for item, price in menu.items():
            if similar(item, itemName):
                itemFound = True
                return item, price
        if itemFound == False:
            return "", -1
    else:
        return "", 0

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    item, price = compareItem(event.message.text)

    if price > 0:
        shoppingCard[item] = price
        msg = "好的！一個{}！".format(item)
    elif price == -1:
        msg = "我們沒有賣{}耶～要不要點點別的？".format(item)
    elif price == 0:
        msg = "您一共點了：\n"
        totalPrice = 0
        for i, p in shoppingCard.items():
            totalPrice += p
            msg += "一個{}，{} 元。\n".format(i, p)
        msg += "這樣一共 {} 元～謝謝惠顧！".format(totalPrice)
        shoppingCard.clear()

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg))


if __name__ == "__main__":
    app.run()
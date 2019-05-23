import os

from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from views.view import View
from views.works_view import WorksView
from views.china_view import ChinaView
from views.shop_view import ShopView
from views.kcoj_view import KcojView
from views.bustw_view import BustwView

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))


@app.route('/callback', methods=['POST'])
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


# 把 view 物件加入觸發機制中
views = [View(), WorksView(), ChinaView(), ShopView(), KcojView(), BustwView()]


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 回應的訊息列表
    responses = []

    # 嘗試觸發各個 view
    for view in views:
        view.trigger(responses, event.message.text)

    # 發送回應
    line_bot_api.reply_message(event.reply_token, responses)


if __name__ == '__main__':
    app.run()

from views.view import View

import random

from linebot.models import (
    TextSendMessage,
)


class OthersView(View):
    def _judge(self, responses: list, text: str) -> bool:
        # 當 responses 的大小為 0 時觸發
        return len(responses) == 0

    def main(self, text: str) -> list:
        """
        隨機回傳一個字串
        """
        sentences = [
            "想聽聽我的自我介紹嗎？",
            "你剛剛說了什麼呢？",
            "不太懂呢...",
            "還是聊點別的吧～",
            "從選單裡找個話題吧！",
        ]

        return [
            TextSendMessage(random.choice(sentences)),
        ]

from views.view import View

from linebot.models import (
    TextSendMessage,
)


class CView(View):
    @property
    def _keywords(self):
        return ['c語言', 'c 語言']

    def main(self, responses: list, text: str) -> None:
        """
        說明自己 C 的程度
        """
        responses += [
            TextSendMessage(
                "大學入學之後馬上面臨到的就是程式設計課，血統純正（？）的資工系學生當然得讓 C 語言給荼毒一下囉。"),
            TextSendMessage(
                "對於基本語法上稱熟悉，但是除了寫作業之外幾乎不會使用到它。"),
        ]

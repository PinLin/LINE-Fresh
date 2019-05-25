from views.view import View

from linebot.models import (
    TextSendMessage,
)


class PythonView(View):
    @property
    def _keywords(self):
        return ['Python']

    def main(self, responses: list, text: str) -> None:
        """
        說明自己 Python 的程度
        """
        responses += [
            TextSendMessage(
                "Python 是我目前最熟練的程式語言，對於基本的語法我都還算是有一定程度的了解。"),
            TextSendMessage(
                "寫出來的程式碼看起來頗整齊讓我是十分喜愛它！"),
            TextSendMessage(
                "平常的一些小專案幾乎都是用它寫的～"),
        ]

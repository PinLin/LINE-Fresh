from views.view import View

from linebot.models import (
    TextSendMessage,
)


class JavaView(View):
    @property
    def _keywords(self):
        return ['java']

    def main(self, text: str) -> list:
        """
        說明自己 Java 的程度
        """
        return [
            TextSendMessage(
                "第一次接觸到 Java 是在修習 Android 應用開發課程時。"),
            TextSendMessage(
                "對於其蓬勃的生態系感到十分驚艷，語法不複雜也是我很喜歡的一點。"),
            TextSendMessage(
                "曾有使用它來練習各種 Design Pattern，但是目前比較不常使用它。"),
        ]

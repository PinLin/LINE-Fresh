from views.view import View

from linebot.models import (
    TextSendMessage,
)


class CsharpView(View):
    @property
    def _keywords(self):
        return ['c#', 'csharp', 'c sharp']

    def main(self, responses: list, text: str) -> None:
        """
        說明自己 C# 的程度
        """
        responses += [
            TextSendMessage(
                "目前對 C# 的印象就是生態系都圍繞在 Windows 上，所以程度大概只有到懂一些基本語法。"),
            TextSendMessage(
                "主要是因為修習學校課程時用它來練習 MVVM 架構，以及影像處理課程的作業是撰寫 C# 的簡單視窗程式。"),
        ]

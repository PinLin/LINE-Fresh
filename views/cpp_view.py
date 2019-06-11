from views.view import View

from linebot.models import (
    TextSendMessage,
)


class CppView(View):
    @property
    def _keywords(self):
        return ['cpp', 'c++', 'cplusplus', 'c plus plus']

    def main(self, text: str) -> list:
        """
        說明自己 C++ 的程度
        """
        return [
            TextSendMessage(
                "是個很麻煩的語言呢，所以也不敢說對它很熟悉"),
            TextSendMessage(
                "因為語言直接內建 OO 概念的關係，很多課都指名要使用它，像是：物件導向程式設計、設計樣式。"),
            TextSendMessage(
                "對於指標操作算是很熟悉，自己寫 Makefile 來編譯也都沒什麼問題。"),
        ]

from linebot.models import TextSendMessage


class View:
    @property
    def _keywords(self) -> list:
        """
        列出所有會觸發此 view 的關鍵字
        """
        return ['測試', 'test']

    def _judge(self, keywords: list, text: str) -> bool:
        """
        設定觸發的條件
        """
        # 如果訊息文字中存在任一關鍵字
        for keyword in self._keywords:
            if keyword.lower() in text.lower():
                return True

        return False

    def trigger(self, responses: list, text: str) -> None:
        """
        觸發 view 的機制
        """
        if self._judge(self._keywords, text):
            self.main(responses, text)

    def main(self, responses: list, text: str) -> None:
        """
        要回傳的所有訊息
        """
        responses += [
            TextSendMessage(text="早安我的朋友"),
        ]

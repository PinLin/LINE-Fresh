from linebot.models import TextSendMessage


class View:
    @property
    def _keywords(self) -> list:
        """
        列出所有會觸發此 view 的關鍵字
        """
        return ['測試', 'test']

    def trigger(self, responses: list, text: str) -> list:
        """
        觸發 view 的機制
        """
        # 如果訊息文字中存在任一關鍵字
        for keyword in self._keywords:
            if keyword.lower() in text.lower():
                # 編輯回應的訊息列表
                return self.main(text)
        
        return []

    def main(self, text: str) -> list:
        """
        要回傳的所有訊息
        """
        return [
            TextSendMessage(text="早安我的朋友"),
        ]

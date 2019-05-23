from views.view import View

from linebot.models import (
    TextSendMessage, StickerSendMessage
)


class KcojView(View):
    @property
    def _keywords(self):
        return ['kcoj', '交作業', 'kcoj.ntut.com.tw']

    def main(self, responses: list, text: str) -> None:
        """
        用簡單文字介紹 KCOJ
        """
        responses += [
            TextSendMessage(
                "這個專案是網頁程式設計課程的期末專題。"),
            TextSendMessage(
                "因為曾經修習過的計算機程式設計課程所使用到的交作業網站有些簡陋，我們便想透過爬蟲程式去操作原先的網站，另外寫一個比較美觀的網站供學弟妹們使用。"),
            TextSendMessage(
                "也算是致敬曾經也有一位學長這麼做過> <"),
            StickerSendMessage(package_id=3, sticker_id=194),
        ]

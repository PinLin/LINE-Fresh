from views.view import View

from linebot.models import (
    TextSendMessage, StickerSendMessage
)


class UrlView(View):
    @property
    def _keywords(self):
        return ['ntut_url', 'url', '縮網址', 'ntut.io/us']

    def main(self, responses: list, text: str) -> None:
        """
        用簡單文字介紹 NTUT_Url
        """
        responses += [
            TextSendMessage(
                text="這個專案是我興趣使然的，會想寫是因為一直在使用的 goo.gl 縮網址服務不再提供了..."),
            TextSendMessage(
                text="然後學校的網路又會對知名的 bit.ly 縮網址服務中間人攻擊（截至 2019-05-23 為止仍是）"),
            TextSendMessage(
                text="剛好趁這個機會來自己實作一個，也覺得如果有自己的縮網址服務很酷ｘＤ"),
            StickerSendMessage(package_id=3, sticker_id=209),
        ]
